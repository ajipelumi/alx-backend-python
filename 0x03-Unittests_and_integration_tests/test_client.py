#!/usr/bin/env python3
""" Test client module. """
import unittest
from unittest.mock import patch, PropertyMock
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

    def test_public_repos_url(self):
        """ Test Public Repos Url property. """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_repo:
            mock_repo.return_value = {"repos_url": "http://abc.com"}
            mock_org = GithubOrgClient("abc")
            expected = mock_repo.return_value["repos_url"]
            result = mock_org._public_repos_url
            self.assertEqual(result, expected)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test Public Repos method. """
        mock_json = [{"name": "Test1"}, {"name": "Test2"}]
        mock_get_json.return_value = mock_json
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:
            mock_public.return_value = "http://abc.com"
            mock_org = GithubOrgClient("abc")
            result = mock_org.public_repos()
            self.assertEqual(result, ["Test1", "Test2"])
            mock_get_json.assert_called_once_with(mock_public.return_value)
            mock_public.assert_called_once_with()


if __name__ == '__main__':
    unittest.main()
