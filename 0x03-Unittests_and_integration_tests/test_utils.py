#!/usr/bin/env python3
"""
Unit Tests
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, param
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test class that inherits from unittest
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 3}}, ("a", "b"), 3),
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """
        Test method for access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, err_message):
        """
        Test method for access_nested_map KeyError
        """
        with self.assertRaises(KeyError) as err:
            access_nested_map(nested_map, path)
        self.assertEqual(str(err.exception), err_message)


class TestGetJson(unittest.TestCase):
    """
    Test class that inherits from unittest
    """
    @parameterized.expand([
        param('http://example.com', {'payload': True}),
        param('http://holberton.io', {'payload': False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test method for get_json
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch('requests.get', return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)


if __name__ == '__main__':
    unittest.main()
