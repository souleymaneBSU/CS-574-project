from __future__ import annotations

import logging
import os

config_text = 'site_name: My Docs\n'
index_text = """# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.
"""

log = logging.getLogger(__name__)


def new(output_dir: str) -> None:

    existing_file_timestamps = []
    if os.path.exists(output_dir):
        # Assert that the project directory exists and no new file created
        assert os.path.isdir(output_dir), f"{output_dir} should be a valid directory."
        for file in os.listdir(output_dir):
            if os.path.isfile(file):
                existing_file_timestamps.append(os.path.getctime(file))
    
    docs_dir = os.path.join(output_dir, 'docs')
    config_path = os.path.join(output_dir, 'mkdocs.yml')
    index_path = os.path.join(docs_dir, 'index.md')

    if os.path.exists(config_path):
        log.info('Project already exists.')
        return

    if not os.path.exists(output_dir):
        log.info(f'Creating project directory: {output_dir}')
        os.mkdir(output_dir)

    log.info(f'Writing config file: {config_path}')
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_text)

    if os.path.exists(index_path):
        return

    log.info(f'Writing initial docs: {index_path}')
    if not os.path.exists(docs_dir):
        os.mkdir(docs_dir)
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_text)

    assert os.path.exists(output_dir), 'Project not successfully created by new command ' + output_dir
    assert all(os.path.getctime(file) in existing_file_timestamps for file in os.listdir(output_dir) if os.path.isfile(file))
