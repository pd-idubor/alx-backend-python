#!/usr/bin/env python3
"""
Unit test
"""
import unittest
from unittest.mock import patch
from parameterized import parameterized, param
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class that inherits from unittest"""

    @parameterized.expand([
        param(org='google'),
        param(org='abc'),
    ])
    @patch('client.get_json')
    def test_org(self, get_mock, org):
        """
        Test method to confirm GithubOrgClient.org returns the correct value
        """
        gitOC = GithubOrgClient(org)
        gitOC.org()
        get_mock.assert_called_once_with(
            'https://api.github.com/orgs/' + org
        )


if __name__ == '__main__':
    unittest.main()
