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

    # de
if __name__ == '__main__':
    unittest.main()
