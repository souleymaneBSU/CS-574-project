#!/usr/bin/env python

import os
import unittest

from mkdocs.commands import new
from mkdocs.tests.base import change_dir, tempdir


class NewTests(unittest.TestCase):
    @tempdir()
    def test_new(self, temp_dir):
        with change_dir(temp_dir):
            new.new("myproject")

            expected_paths = [
                os.path.join(temp_dir, "myproject"),
                os.path.join(temp_dir, "myproject", "mkdocs.yml"),
                os.path.join(temp_dir, "myproject", "docs"),
                os.path.join(temp_dir, "myproject", "docs", "index.md"),
            ]

            for expected_path in expected_paths:
                self.assertTrue(os.path.exists(expected_path))

    @tempdir()
    def test_new_config_exists(self, temp_dir):
        with change_dir(temp_dir):
            
            existing_config = os.path.join("myproject", "mkdocs.yml")

            os.mkdir('myproject')

            with open(f'./{existing_config}', 'w') as config_file:
                config_file.write('create temp config file')

            new.new("myproject")

            expected_paths = [
                os.path.join(temp_dir, "myproject", "docs"),
                os.path.join(temp_dir, "myproject", "docs", "index.md"),
            ]

            for expected_path in expected_paths:
                self.assertFalse(os.path.exists(expected_path))

    @tempdir()
    def test_new_index_exists(self, temp_dir):
        with change_dir(temp_dir):
            
            existing_index = os.path.join("myproject", "docs", "index.md")

            os.mkdir('myproject')
            os.mkdir('myproject/docs')

            with open(existing_index, 'w') as config_file:
                config_file.write('create temp config file')

            new.new("myproject")

            expected_paths = [
                os.path.join(temp_dir, "myproject"),
                os.path.join(temp_dir, "myproject", "mkdocs.yml"),
                os.path.join(temp_dir, "myproject", "docs"),
                os.path.join(temp_dir, "myproject", "docs", "index.md"),
            ]

            for expected_path in expected_paths:
                self.assertTrue(os.path.exists(expected_path))

    @tempdir()
    def test_new_docs_dir_exists(self, temp_dir):
        with change_dir(temp_dir):
            
            os.mkdir('myproject')
            os.mkdir('myproject/docs')

            new.new("myproject")

            expected_paths = [
                os.path.join(temp_dir, "myproject"),
                os.path.join(temp_dir, "myproject", "mkdocs.yml"),
                os.path.join(temp_dir, "myproject", "docs"),
                os.path.join(temp_dir, "myproject", "docs", "index.md"),
            ]

            for expected_path in expected_paths:
                self.assertTrue(os.path.exists(expected_path))
