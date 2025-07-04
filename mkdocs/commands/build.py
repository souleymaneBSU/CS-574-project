from __future__ import annotations

import gzip
import logging
import os
import time
from typing import TYPE_CHECKING, Sequence
from urllib.parse import urljoin, urlsplit

import jinja2
from jinja2.exceptions import TemplateNotFound

import mkdocs
from mkdocs import utils
from mkdocs.exceptions import Abort, BuildError
from mkdocs.structure.files import File, Files, InclusionLevel, get_files, set_exclusions
from mkdocs.structure.nav import Navigation, get_navigation
from mkdocs.structure.pages import Page
from mkdocs.utils import DuplicateFilter  # noqa: F401 - legacy re-export
from mkdocs.utils import templates

if TYPE_CHECKING:
    from mkdocs.config.defaults import MkDocsConfig


log = logging.getLogger(__name__)
_get_context_called: bool = False


def get_context(
    nav: Navigation,
    files: Sequence[File] | Files,
    config: MkDocsConfig,
    page: Page | None = None,
    base_url: str = '',
) -> templates.TemplateContext:
    """Return the template context for a given page or template."""
    global _get_context_called
    if page is not None:
        base_url = utils.get_relative_url('.', page.url)

    extra_javascript = [
        utils.normalize_url(str(script), page, base_url) for script in config.extra_javascript
    ]
    extra_css = [utils.normalize_url(path, page, base_url) for path in config.extra_css]

    if isinstance(files, Files):
        files = files.documentation_pages()

    assert config._load_dict_called == True and config._validate_called == True 
    _get_context_called = True
    return templates.TemplateContext(
        nav=nav,
        pages=files,
        base_url=base_url,
        extra_css=extra_css,
        extra_javascript=extra_javascript,
        mkdocs_version=mkdocs.__version__,
        build_date_utc=utils.get_build_datetime(),
        config=config,
        page=page,
    )


def _build_template(
    name: str, template: jinja2.Template, files: Files, config: MkDocsConfig, nav: Navigation
) -> str:
    """Return rendered output for given template as a string."""
    # Run `pre_template` plugin events.
    template = config.plugins.on_pre_template(template, template_name=name, config=config)

    if utils.is_error_template(name):
        # Force absolute URLs in the nav of error pages and account for the
        # possibility that the docs root might be different than the server root.
        # See https://github.com/mkdocs/mkdocs/issues/77.
        # However, if site_url is not set, assume the docs root and server root
        # are the same. See https://github.com/mkdocs/mkdocs/issues/1598.
        base_url = urlsplit(config.site_url or '/').path
    else:
        base_url = utils.get_relative_url('.', name)

    context = get_context(nav, files, config, base_url=base_url)

    # Run `template_context` plugin events.
    context = config.plugins.on_template_context(context, template_name=name, config=config)

    output = template.render(context)

    # Run `post_template` plugin events.
    output = config.plugins.on_post_template(output, template_name=name, config=config)

    return output


def _build_theme_template(
    template_name: str, env: jinja2.Environment, files: Files, config: MkDocsConfig, nav: Navigation
) -> None:
    """Build a template using the theme environment."""
    log.debug(f"Building theme template: {template_name}")

    try:
        template = env.get_template(template_name)
    except TemplateNotFound:
        log.warning(f"Template skipped: '{template_name}' not found in theme directories.")
        return

    output = _build_template(template_name, template, files, config, nav)

    if output.strip():
        output_path = os.path.join(config.site_dir, template_name)
        utils.write_file(output.encode('utf-8'), output_path)

        if template_name == 'sitemap.xml':
            log.debug(f"Gzipping template: {template_name}")
            gz_filename = f'{output_path}.gz'
            with open(gz_filename, 'wb') as f:
                timestamp = utils.get_build_timestamp(
                    pages=[f.page for f in files.documentation_pages() if f.page is not None]
                )
                with gzip.GzipFile(
                    fileobj=f, filename=gz_filename, mode='wb', mtime=timestamp
                ) as gz_buf:
                    gz_buf.write(output.encode('utf-8'))
    else:
        log.info(f"Template skipped: '{template_name}' generated empty output.")


def _build_extra_template(template_name: str, files: Files, config: MkDocsConfig, nav: Navigation):
    """Build user templates which are not part of the theme."""
    log.debug(f"Building extra template: {template_name}")

    file = files.get_file_from_path(template_name)
    if file is None:
        log.warning(f"Template skipped: '{template_name}' not found in docs_dir.")
        return

    try:
        template = jinja2.Template(file.content_string)
    except Exception as e:
        log.warning(f"Error reading template '{template_name}': {e}")
        return

    output = _build_template(template_name, template, files, config, nav)

    if output.strip():
        utils.write_file(output.encode('utf-8'), file.abs_dest_path)
    else:
        log.info(f"Template skipped: '{template_name}' generated empty output.")


def _populate_page(page: Page, config: MkDocsConfig, files: Files, dirty: bool = False) -> None:
    """Read page content from docs_dir and render Markdown."""
    config._current_page = page
    try:
        # When --dirty is used, only read the page if the file has been modified since the
        # previous build of the output.
        if dirty and not page.file.is_modified():
            return

        # Run the `pre_page` plugin event
        page = config.plugins.on_pre_page(page, config=config, files=files)

        page.read_source(config)
        assert page.markdown is not None

        # Run `page_markdown` plugin events.
        page.markdown = config.plugins.on_page_markdown(
            page.markdown, page=page, config=config, files=files
        )

        page.render(config, files)
        assert page.content is not None

        # Run `page_content` plugin events.
        page.content = config.plugins.on_page_content(
            page.content, page=page, config=config, files=files
        )
    except Exception as e:
        message = f"Error reading page '{page.file.src_uri}':"
        # Prevent duplicated the error message because it will be printed immediately afterwards.
        if not isinstance(e, BuildError):
            message += f" {e}"
        log.error(message)
        raise
    finally:
        config._current_page = None


def _build_page(
    page: Page,
    config: MkDocsConfig,
    doc_files: Sequence[File],
    nav: Navigation,
    env: jinja2.Environment,
    dirty: bool = False,
    excluded: bool = False,
) -> None:
    """Pass a Page to theme template and write output to site_dir."""
    config._current_page = page
    try:
        # When --dirty is used, only build the page if the file has been modified since the
        # previous build of the output.
        if dirty and not page.file.is_modified():
            return

        log.debug(f"Building page {page.file.src_uri}")

        # Activate page. Signals to theme that this is the current page.
        page.active = True

        context = get_context(nav, doc_files, config, page)

        # Allow 'template:' override in md source files.
        template = env.get_template(page.meta.get('template', 'main.html'))

        # Run `page_context` plugin events.
        context = config.plugins.on_page_context(context, page=page, config=config, nav=nav)

        if excluded:
            page.content = (
                '<div class="mkdocs-draft-marker" title="This page will not be included into the built site.">'
                'DRAFT'
                '</div>' + (page.content or '')
            )

        # Render the template.
        output = template.render(context)

        # Run `post_page` plugin events.
        output = config.plugins.on_post_page(output, page=page, config=config)

        # Write the output file.
        if output.strip():
            utils.write_file(
                output.encode('utf-8', errors='xmlcharrefreplace'), page.file.abs_dest_path
            )
        else:
            log.info(f"Page skipped: '{page.file.src_uri}'. Generated empty output.")

    except Exception as e:
        message = f"Error building page '{page.file.src_uri}':"
        # Prevent duplicated the error message because it will be printed immediately afterwards.
        if not isinstance(e, BuildError):
            message += f" {e}"
        log.error(message)
        raise
    finally:
        # Deactivate page
        page.active = False
        config._current_page = None


def build(config: MkDocsConfig, *, serve_url: str | None = None, dirty: bool = False) -> None:
    """Perform a full site build."""
    global _get_context_called
    logger = logging.getLogger('mkdocs')

    # Add CountHandler for strict mode
    warning_counter = utils.CountHandler()
    warning_counter.setLevel(logging.WARNING)
    if config.strict:
        logging.getLogger('mkdocs').addHandler(warning_counter)

    inclusion = InclusionLevel.is_in_serve if serve_url else InclusionLevel.is_included

    try:
        start = time.monotonic()

        # Run `config` plugin events.
        config = config.plugins.on_config(config)

        # Run `pre_build` plugin events.
        config.plugins.on_pre_build(config=config)

        if not dirty:
            log.info("Cleaning site directory")
            utils.clean_directory(config.site_dir)
        else:  # pragma: no cover
            # Warn user about problems that may occur with --dirty option
            log.warning(
                "A 'dirty' build is being performed, this will likely lead to inaccurate navigation and other"
                " links within your site. This option is designed for site development purposes only."
            )

        if not serve_url:  # pragma: no cover
            log.info(f"Building documentation to directory: {config.site_dir}")
            if dirty and site_directory_contains_stale_files(config.site_dir):
                log.info("The directory contains stale files. Use --clean to remove them.")

        # First gather all data from all files/pages to ensure all data is consistent across all pages.

        files = get_files(config)
        env = config.theme.get_env()
        files.add_files_from_theme(env, config)

        assert len(set([file.src_dir for file in files])) == 2 + len(config['plugins']), 'Count of distinct directories does not match the expected count'

        # Run `files` plugin events.
        files = config.plugins.on_files(files, config=config)
        # If plugins have added files but haven't set their inclusion level, calculate it again.
        set_exclusions(files, config)

        nav = get_navigation(files, config)

        # Run `nav` plugin events.
        nav = config.plugins.on_nav(nav, config=config, files=files)

        log.debug("Reading markdown pages.")
        excluded = []
        for file in files.documentation_pages(inclusion=inclusion):
            log.debug(f"Reading: {file.src_uri}")
            if file.page is None and file.inclusion.is_not_in_nav():
                if serve_url and file.inclusion.is_excluded():
                    excluded.append(urljoin(serve_url, file.url))
                Page(None, file, config)
            assert file.page is not None
            _populate_page(file.page, config, files, dirty)
        if excluded:
            log.info(
                "The following pages are being built only for the preview "
                "but will be excluded from `mkdocs build` per `draft_docs` config:\n  - "
                + "\n  - ".join(excluded)
            )

        # Run `env` plugin events.
        env = config.plugins.on_env(env, config=config, files=files)

        # Start writing files to site_dir now that all data is gathered. Note that order matters. Files
        # with lower precedence get written first so that files with higher precedence can overwrite them.

        log.debug("Copying static assets.")
        files.copy_static_files(dirty=dirty, inclusion=inclusion)

        for template in config.theme.static_templates:
            _build_theme_template(template, env, files, config, nav)

        for template in config.extra_templates:
            _build_extra_template(template, files, config, nav)

        log.debug("Building markdown pages.")
        doc_files = files.documentation_pages(inclusion=inclusion)
        for file in doc_files:
            assert file.page is not None
            _get_context_called = False
            _build_page(
                file.page, config, doc_files, nav, env, dirty, excluded=file.inclusion.is_excluded()
            )
            assert _get_context_called, 'Context not set as expected, config may be invalid'

        log_level = config.validation.links.anchors
        for file in doc_files:
            assert file.page is not None
            file.page.validate_anchor_links(files=files, log_level=log_level)

        # Run `post_build` plugin events.
        config.plugins.on_post_build(config=config)

        if counts := warning_counter.get_counts():
            msg = ', '.join(f'{v} {k.lower()}s' for k, v in counts)
            raise Abort(f'Aborted with {msg} in strict mode!')

        log.info(f'Documentation built in {time.monotonic() - start:.2f} seconds')

        assert all(file.inclusion != InclusionLevel.UNDEFINED for file in files), 'File used in build with UNDEFINED inclusion'
        assert all([compfile for compfile in files.documentation_pages()].count(file) == 1 for file in files.documentation_pages()), 'Duplicate file found'
        assert all(os.path.exists(file.abs_dest_path) for file in files if file.inclusion.is_included()), 'An included file was not rendered'
        assert not any(env.get_template(template) for template in config.theme.static_templates) or os.path.exists(os.path.join(config.site_dir, '404.html')), 'Theme exists and 404 file was not copied from the theme'

    except Exception as e:
        # Run `build_error` plugin events.
        config.plugins.on_build_error(error=e)
        if isinstance(e, BuildError):
            log.error(str(e))
            raise Abort('Aborted with a BuildError!')
        raise

    finally:
        logger.removeHandler(warning_counter)


def site_directory_contains_stale_files(site_directory: str) -> bool:
    """Check if the site directory contains stale files from a previous build."""
    return bool(os.path.exists(site_directory) and os.listdir(site_directory))
