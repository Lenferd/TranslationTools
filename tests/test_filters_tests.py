#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest

# sys.path.append(os.path.join("..", ".."))
from Modules.TextOperations import text_filter


class TestTextOperationsMethods(unittest.TestCase):
    def is_have_underscore_return_true_with_underscore_str(self):
        test_line = "test_test"

        self.assertTrue(text_filter.is_have_underscore(test_line))

    # def is_have_

if __name__ == '__main__':
    unittest.main()
