#!/usr/bin/env python3
""" Test client module. """
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """ Github Org Client Test Class. """
    @parameterized.expand([
        ("google", {"org": "google", "year": 2023}),
        ("abc", {"org": "abc", "year": 2024})
    ])
    @patch('client.get_json')
    def test_org(self, org, expected_result, mock_get_json):
        """ Test GithubOrgClient.org method. """
        mock_get_json.return_value = expected_result
        test_class = GithubOrgClient(org)
        self.assertEqual(test_class.org, expected_result)
        url = 'https://api.github.com/orgs/{}'.format(org)
        mock_get_json.assert_called_once_with(url)


if __name__ == '__main__':
    unittest.main()
