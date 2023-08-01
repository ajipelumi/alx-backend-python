#!/usr/bin/env python3
""" Test client module. """
import unittest
from unittest.mock import patch, PropertyMock, Mock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class


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

    @parameterized.expand([
        ({'license': {'key': 'my_license'}}, 'my_license', True),
        ({'license': {'key': 'other_license'}}, 'my_license', False)
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """ Test Has License method. """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": TEST_PAYLOAD[0][0],
        "repos_payload": TEST_PAYLOAD[0][1],
        "expected_repos": TEST_PAYLOAD[0][2],
        "apache2_repos": TEST_PAYLOAD[0][3]
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ Integration test for GithubOrgClient. """
    @classmethod
    def setUpClass(cls):
        """ Set up class method. """
        # Create a dict of payloads to be used in mocked `get` requests.
        # Key is the URL to mock, value is the JSON payload to return.
        # The values was passed as parameterized class.
        payloads = {
            "https://api.github.com/orgs/google": cls.org_payload,
            "https://api.github.com/orgs/google/repos": cls.repos_payload
        }

        # Create a function that takes a URL and returns a mock response.
        def get_payload(url):
            """ Get payload method. """
            # If the URL is one of the payloads, return the associated value.
            if url in payloads:
                return Mock(ok=True, json=lambda: payloads[url])
            return Mock(ok=False)

        # Patch `requests.get` to return our function's mock response.
        cls.get_patcher = patch('requests.get', side_effect=get_payload)
        # Start patcher.
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ Tear down class method. """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ Test Public Repos method. """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """ Test Public Repos with License method. """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos("apache-2.0"),
                         self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
