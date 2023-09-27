#!/usr/bin/env python3
"""
Unit Tests
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, param
from utils import access_nested_map
from utils import get_json
from utils import memoize


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
        param("http://example.com", {"payload": True}),
        param("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """
        Test method for get_json
        """
        mock = Mock()
        mock.json.return_value = test_payload
        with patch("requests.get", return_value=mock):
            self.assertEqual(get_json(test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """
    Test class that inherits from unittest
    """

    def test_memoize(self):
        """
        Test method for test_memoize
        """
        class TestClass:
            """
            Test class
            """

            def a_method(self):
                """
                Test method for a_method
                """
                return 42

            @memoize
            def a_property(self):
                """
                Test method for a_property
                """
                return self.a_method()

        test = TestClass()
        with patch.object(test, "a_method") as mock_a_method:
            test.a_property()
            test.a_property()

            mock_a_method.assert_called_once()


if __name__ == "__main__":
    unittest.main()
