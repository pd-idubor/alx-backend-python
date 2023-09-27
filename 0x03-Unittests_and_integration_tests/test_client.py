#!/usr/bin/env python3
"""
Unit test
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, param, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @patch('client.get_json')
    def test_public_repos(self, get_mock):
        """
        Test for GithubOrgClient.public_repos
        """
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_url:

            mock_url.return_value = 'http://some_url'
            get_mock.return_value = [
                {'name': 'google'}, {'name': 'abc'}
            ]
            gitOC = GithubOrgClient('test')

            self.assertEqual(gitOC.public_repos(), ['google', 'abc'])
            mock_url.assert_called_once_with()
            get_mock.assert_called_once_with('http://some_url')

    @parameterized.expand([
        param(input_payload={'license': {'key': 'my_license'}},
              expected_license_key='my_license'),
        param(input_payload={'license': {'key': 'other_license'}},
              expected_license_key='other_license'),
    ])
    def test_has_license(self, input_payload, expected_license_key):
        """
        Test for GithubOrgClient.has_license
        """
        gitOC = GithubOrgClient('test')
        self.assertEqual(gitOC.has_license(
            input_payload, expected_license_key), True)


@parameterized_class(['org_payload', 'repos_payload',
                      'expected_repos', 'apache2_repos'], TEST_PAYLOAD)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Test class that inherits from unittest"""

    @classmethod
    def setUpClass(cls):
        """
        Setup method
        """
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload,
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """
        Teardown method
        """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
