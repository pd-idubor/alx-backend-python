#!/usr/bin/env python3
"""
unit test for utils.access_nested_map.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    test class that inherits from unittest
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 3}}, ("a", "b"), 3),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        '''
        test method for access_nested_map
        '''
        self.assertEqual(access_nested_map(nested_map, path), result)


if __name__ == '__main__':
    unittest.main()
