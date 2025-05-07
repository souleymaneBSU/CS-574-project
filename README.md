## Team members

Matt Smith, Souleymane Cheikh Sidia

## Assertions

mkdocs/commands/build.py 50, 296, 348, 364-367 
mkdocs/commands/new.py 62, 63 
mkdocs/commands/serve.py 57 
mkdocs/livereload/__init__.py (serve) 198, 232, 233

mkdocs/config/base.py: 234, 310, 311, 352-357, 412-413

mkdocs/structure/nav.py: 135, 191-195
mkdocs/structure/files.py: 588,589
mkdocs/structure/pages.py: 249. 273, 306-307
mkdocs/structure/toc.py: 21, 83

## Commands

### Package install

pip install coverage pytest pyre fb-sapp

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
