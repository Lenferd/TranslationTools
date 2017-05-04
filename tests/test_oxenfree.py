#!/usr/bin/python3
# -*- coding: utf-8 -*-

import unittest
from Modules.TextOperations import text_filter


class TestTextOperationsMethods(unittest.TestCase):
    def test_not_remove_uppercase_name(self):
        name = [["REN"]]

        result, removed = text_filter.oxenfree_filter_resources(name)

        expected = [["REN"]]
        self.assertEqual(result, expected)

    def test_remove_Unity_data(self):
        data = [["REN", "test str", "Unity.system.str"]]

        result, removed = text_filter.oxenfree_filter_resources(data)

        expected_result = [["REN", "test str"]]
        self.assertEqual(result, expected_result)
        # self.assertEqual(removed, expected)


if __name__ == '__main__':
    unittest.main()
