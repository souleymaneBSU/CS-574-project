## Team members

Matt Smith, Souleymane Cheikh Sidia

## Assertions

mkdocs/config/base.py: 301-203
mkdocs/config/base.py: 344-348
mkdocs/config/base.py: 403-404

mkdocs/structure/nav.py: 133
mkdocs/structure/nav.py: 191-196

mkdocs/structure/pages.py: 306-308
mkdocs/structure/toc.py: 21
mkdocs/structure/toc.py: 83

Single item nav todo

# Testing

Before additional tests: Stmts 3776    Miss 380   Br 1140    BrPart 127    Percentage88%
After:  Stmts 3776    Miss 374   Br 1140    BrPart 119    prct 89%

## Commands

### Coverity

~/Downloads/cov-analysis-linux64-2024.6.1/bin/cov-build --dir cov-int --no-command --fs-capture-search mkdocs

tar czvf dataflow.tgz cov-int/

### pyre
pyre

### pysa
pyre analyze --save-results-to ./pysa-runs
cd pysa-runs
sapp analyze ./taint-output.json


## Additional Tests:

test_do_not_find_toc_by_id
test_new_docs_dir_exists
test_new_index_exists
test_new_config_exists
test_handling_bad_config_with_one_item
test_nav_with_excluded_file_in_nav
test_nav_with_excluded_file_not_in_nav
test_nav_with_excluded_file_no_nav
