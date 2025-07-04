# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import mkdocs.contrib.search.search_index as module_0


def test_case_0():
    search_index_0 = module_0.SearchIndex()
    assert module_0.haslunrpy is False


def test_case_1():
    str_0 = ".)N,Ku-"
    list_0 = [str_0]
    content_section_0 = module_0.ContentSection(list_0, str_0)
    assert content_section_0.text == [".)N,Ku-"]
    assert module_0.haslunrpy is False


def test_case_2():
    content_section_0 = module_0.ContentSection()
    assert content_section_0.text == []
    assert module_0.haslunrpy is False


def test_case_3():
    content_parser_0 = module_0.ContentParser()
    assert content_parser_0.convert_charrefs is True
    assert content_parser_0.rawdata == ""
    assert content_parser_0.lasttag == "???"
    assert (
        f"{type(content_parser_0.interesting).__module__}.{type(content_parser_0.interesting).__qualname__}"
        == "re.Pattern"
    )
    assert content_parser_0.cdata_elem is None
    assert content_parser_0.lineno == 1
    assert content_parser_0.offset == 0
    assert content_parser_0.data == []
    assert content_parser_0.section is None
    assert content_parser_0.is_header_tag is False
    assert module_0.haslunrpy is False
    assert (
        f"{type(module_0.ContentParser.stripped_html).__module__}.{type(module_0.ContentParser.stripped_html).__qualname__}"
        == "builtins.property"
    )
    str_0 = ".md"
    tuple_0 = (str_0, str_0)
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    none_type_0 = content_parser_0.handle_starttag(str_0, list_0)


def test_case_4():
    content_parser_0 = module_0.ContentParser()
    assert content_parser_0.convert_charrefs is True
    assert content_parser_0.rawdata == ""
    assert content_parser_0.lasttag == "???"
    assert (
        f"{type(content_parser_0.interesting).__module__}.{type(content_parser_0.interesting).__qualname__}"
        == "re.Pattern"
    )
    assert content_parser_0.cdata_elem is None
    assert content_parser_0.lineno == 1
    assert content_parser_0.offset == 0
    assert content_parser_0.data == []
    assert content_parser_0.section is None
    assert content_parser_0.is_header_tag is False
    assert module_0.haslunrpy is False
    assert (
        f"{type(module_0.ContentParser.stripped_html).__module__}.{type(module_0.ContentParser.stripped_html).__qualname__}"
        == "builtins.property"
    )


def test_case_5():
    content_section_0 = module_0.ContentSection()
    assert content_section_0.text == []
    assert module_0.haslunrpy is False
    var_0 = content_section_0.__eq__(content_section_0)
    assert var_0 is True


def test_case_6():
    content_parser_0 = module_0.ContentParser()
    assert content_parser_0.convert_charrefs is True
    assert content_parser_0.rawdata == ""
    assert content_parser_0.lasttag == "???"
    assert (
        f"{type(content_parser_0.interesting).__module__}.{type(content_parser_0.interesting).__qualname__}"
        == "re.Pattern"
    )
    assert content_parser_0.cdata_elem is None
    assert content_parser_0.lineno == 1
    assert content_parser_0.offset == 0
    assert content_parser_0.data == []
    assert content_parser_0.section is None
    assert content_parser_0.is_header_tag is False
    assert module_0.haslunrpy is False
    assert (
        f"{type(module_0.ContentParser.stripped_html).__module__}.{type(module_0.ContentParser.stripped_html).__qualname__}"
        == "builtins.property"
    )
    content_section_0 = module_0.ContentSection(content_parser_0, content_parser_0)
    assert (
        f"{type(content_section_0.text).__module__}.{type(content_section_0.text).__qualname__}"
        == "mkdocs.contrib.search.search_index.ContentParser"
    )
    str_0 = "5"
    none_type_0 = content_parser_0.handle_endtag(str_0)
    none_type_1 = content_parser_0.handle_starttag(str_0, str_0)
    var_0 = content_parser_0.handle_data(content_parser_0)


def test_case_7():
    content_parser_0 = module_0.ContentParser()
    assert content_parser_0.convert_charrefs is True
    assert content_parser_0.rawdata == ""
    assert content_parser_0.lasttag == "???"
    assert (
        f"{type(content_parser_0.interesting).__module__}.{type(content_parser_0.interesting).__qualname__}"
        == "re.Pattern"
    )
    assert content_parser_0.cdata_elem is None
    assert content_parser_0.lineno == 1
    assert content_parser_0.offset == 0
    assert content_parser_0.data == []
    assert content_parser_0.section is None
    assert content_parser_0.is_header_tag is False
    assert module_0.haslunrpy is False
    assert (
        f"{type(module_0.ContentParser.stripped_html).__module__}.{type(module_0.ContentParser.stripped_html).__qualname__}"
        == "builtins.property"
    )
    none_type_0 = None
    none_type_1 = content_parser_0.handle_data(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_8():
    content_parser_0 = module_0.ContentParser()
    assert content_parser_0.convert_charrefs is True
    assert content_parser_0.rawdata == ""
    assert content_parser_0.lasttag == "???"
    assert (
        f"{type(content_parser_0.interesting).__module__}.{type(content_parser_0.interesting).__qualname__}"
        == "re.Pattern"
    )
    assert content_parser_0.cdata_elem is None
    assert content_parser_0.lineno == 1
    assert content_parser_0.offset == 0
    assert content_parser_0.data == []
    assert content_parser_0.section is None
    assert content_parser_0.is_header_tag is False
    assert module_0.haslunrpy is False
    assert (
        f"{type(module_0.ContentParser.stripped_html).__module__}.{type(module_0.ContentParser.stripped_html).__qualname__}"
        == "builtins.property"
    )
    content_section_0 = module_0.ContentSection(content_parser_0, content_parser_0)
    assert (
        f"{type(content_section_0.text).__module__}.{type(content_section_0.text).__qualname__}"
        == "mkdocs.contrib.search.search_index.ContentParser"
    )
    content_section_1 = module_0.ContentSection()
    assert content_section_1.text == []
    var_0 = content_section_1.__eq__(content_section_0)
    assert var_0 is False
    var_1 = content_parser_0.handle_comment(content_section_0)
    var_0.handle_endtag(var_1)
