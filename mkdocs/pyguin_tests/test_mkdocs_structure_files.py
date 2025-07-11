# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mkdocs.structure.files as module_0
import tokenize as module_1


def test_case_0():
    pass


def test_case_1():
    str_0 = "A commit message to use when committing to the GitHub Pages remote branch. Commit {sha} and MkDocs {version} are available as expansions"
    none_type_0 = None
    bool_0 = True
    file_0 = module_0.File(
        str_0, none_type_0, str_0, bool_0, dest_uri=str_0, inclusion=str_0
    )
    assert (
        file_0.src_uri
        == "A commit message to use when committing to the GitHub Pages remote branch. Commit {sha} and MkDocs {version} are available as expansions"
    )
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )


def test_case_2():
    str_0 = "'1oU*%\"+ 4rFE;?F"
    bool_0 = True
    file_0 = module_0.File(str_0, str_0, str_0, bool_0)
    assert file_0.src_uri == "'1oU*%\"+ 4rFE;?F"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )


@pytest.mark.xfail(strict=True)
def test_case_3():
    var_0 = module_1.any()
    module_0.Files(var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    module_0.File(bool_0, bool_0, bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "w:E0|CXLE>"
    bool_0 = True
    file_0 = module_0.File(str_0, str_0, str_0, bool_0)
    assert file_0.src_uri == "w:E0|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    file_0.is_media_file()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "w:E0|CXLE>"
    bool_0 = True
    file_0 = module_0.File(str_0, str_0, str_0, bool_0)
    assert file_0.src_uri == "w:E0|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    file_0.copy_file()


@pytest.mark.xfail(strict=True)
def test_case_7():
    str_0 = "w:VE|CXLE>"
    bool_0 = True
    none_type_0 = None
    file_0 = module_0.File(
        str_0, none_type_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "w:VE|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    var_0 = file_0.__repr__()
    assert (
        var_0
        == "File('w:VE|CXLE>', src_dir=None, dest_dir='w:VE|CXLE>', use_directory_urls=True, dest_uri='w:VE|CXLE>', inclusion=None)"
    )
    assert file_0.dest_uri == "w:VE|CXLE>"
    str_1 = file_0.url_relative_to(str_0)
    assert str_1 == "../w%3AVE%7CCXLE%3E"
    assert file_0.url == "w%3AVE%7CCXLE%3E"
    file_0.is_media_file()


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "h s}HPA68N}-QCdin"
    set_0 = {str_0}
    bool_0 = False
    none_type_0 = None
    file_0 = module_0.File(
        str_0, set_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "h s}HPA68N}-QCdin"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    file_0.is_javascript()


def test_case_9():
    str_0 = "h s}P68N}-QCdin"
    set_0 = set()
    bool_0 = False
    none_type_0 = None
    file_0 = module_0.File(
        str_0, set_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "h s}P68N}-QCdin"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    var_0 = module_0.file_sort_key(file_0)
    assert file_0.name == "h s}P68N}-QCdin"


def test_case_10():
    str_0 = "w:E|CXLE>"
    bool_0 = True
    none_type_0 = None
    file_0 = module_0.File(
        str_0, none_type_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "w:E|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    str_1 = file_0.url_relative_to(str_0)
    assert str_1 == "../w%3AE%7CCXLE%3E"
    assert file_0.dest_uri == "w:E|CXLE>"
    assert file_0.url == "w%3AE%7CCXLE%3E"
    bool_1 = file_0.is_css()
    assert bool_1 is False
    bool_2 = False
    with pytest.raises(AssertionError):
        file_0.copy_file(bool_2)


@pytest.mark.xfail(strict=True)
def test_case_11():
    str_0 = 'w:E0|C"LE>'
    none_type_0 = None
    file_0 = module_0.File(str_0, str_0, str_0, none_type_0)
    assert file_0.src_uri == 'w:E0|C"LE>'
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    str_1 = file_0.url_relative_to(str_0)
    assert str_1 == "../w%3AE0%7CC%22LE%3E"
    assert file_0.dest_uri == 'w:E0|C"LE>'
    assert file_0.url == "w%3AE0%7CC%22LE%3E"
    bool_0 = True
    none_type_1 = file_0.copy_file(bool_0)


def test_case_12():
    str_0 = "w:VE|CXLE>"
    bool_0 = True
    none_type_0 = None
    file_0 = module_0.File(
        str_0, none_type_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "w:VE|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    str_1 = file_0.url_relative_to(str_0)
    assert str_1 == "../w%3AVE%7CCXLE%3E"
    assert file_0.dest_uri == "w:VE|CXLE>"
    assert file_0.url == "w%3AVE%7CCXLE%3E"


def test_case_13():
    str_0 = "w:E|CXLE>"
    bool_0 = True
    none_type_0 = None
    file_0 = module_0.File(
        str_0, none_type_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "w:E|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    str_1 = file_0.url_relative_to(str_0)
    assert str_1 == "../w%3AE%7CCXLE%3E"
    assert file_0.dest_uri == "w:E|CXLE>"
    assert file_0.url == "w%3AE%7CCXLE%3E"
    with pytest.raises(AssertionError):
        file_0.copy_file()


def test_case_14():
    str_0 = "w:E|CXLE>"
    bool_0 = True
    none_type_0 = None
    file_0 = module_0.File(
        str_0, none_type_0, str_0, bool_0, dest_uri=none_type_0, inclusion=none_type_0
    )
    assert file_0.src_uri == "w:E|CXLE>"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    str_1 = file_0.url_relative_to(str_0)
    assert str_1 == "../w%3AE%7CCXLE%3E"
    assert file_0.dest_uri == "w:E|CXLE>"
    assert file_0.url == "w%3AE%7CCXLE%3E"
    bool_1 = True
    with pytest.raises(AssertionError):
        file_0.copy_file(bool_1)


@pytest.mark.xfail(strict=True)
def test_case_15():
    bool_0 = True
    str_0 = "tpaL}-zV1m#w&.X[-$"
    str_1 = "nXV2"
    file_0 = module_0.File(str_1, str_0, str_1, bool_0)
    assert file_0.src_uri == "nXV2"
    assert (
        f"{type(module_0.File.src_path).__module__}.{type(module_0.File.src_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.dest_path).__module__}.{type(module_0.File.dest_path).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.generated).__module__}.{type(module_0.File.generated).__qualname__}"
        == "builtins.method"
    )
    assert (
        f"{type(module_0.File.edit_uri).__module__}.{type(module_0.File.edit_uri).__qualname__}"
        == "mkdocs.utils.weak_property"
    )
    assert (
        f"{type(module_0.File.abs_src_path).__module__}.{type(module_0.File.abs_src_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_src_path.attrname == "abs_src_path"
    assert (
        f"{type(module_0.File.abs_src_path.lock).__module__}.{type(module_0.File.abs_src_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.abs_dest_path).__module__}.{type(module_0.File.abs_dest_path).__qualname__}"
        == "functools.cached_property"
    )
    assert module_0.File.abs_dest_path.attrname == "abs_dest_path"
    assert (
        f"{type(module_0.File.abs_dest_path.lock).__module__}.{type(module_0.File.abs_dest_path.lock).__qualname__}"
        == "_thread.RLock"
    )
    assert (
        f"{type(module_0.File.content_bytes).__module__}.{type(module_0.File.content_bytes).__qualname__}"
        == "builtins.property"
    )
    assert (
        f"{type(module_0.File.content_string).__module__}.{type(module_0.File.content_string).__qualname__}"
        == "builtins.property"
    )
    str_2 = file_0.url_relative_to(file_0)
    assert str_2 == "."
    assert file_0.dest_uri == "nXV2"
    assert file_0.url == "nXV2"
    file_0.copy_file(str_1)
