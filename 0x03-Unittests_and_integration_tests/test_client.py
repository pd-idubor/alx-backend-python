#!/usr/bin/env python3
"""
Unit test
"""
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """
        Test result of _public_repos_url based on the mocked payload
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:
            mock_url.return_value = 'http://some_url'
            gitOC = GithubOrgClient('test')
            self.assertEqual(gitOC._public_repos_url,
                             'http://some_url')
            mock_url.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
