#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

from Modules.TextOperations import text_filter


class TestTextOperationsMethods(unittest.TestCase):
    def tests_working(self):
        self.assertTrue(1 == 1)

    def test_is_have_underscore_return_true_with_underscore_str(self):
        test_line = "test_test"

        self.assertTrue(text_filter.is_have_underscore(test_line))

    def test_get_true_for_system_str(self):
        test_line = "Unity.sys.test"

        self.assertTrue(text_filter.is_have_unity_system_string(test_line))

if __name__ == '__main__':
    unittest.main()
