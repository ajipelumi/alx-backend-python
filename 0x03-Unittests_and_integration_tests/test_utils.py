#!/usr/bin/env python3
""" Test utils module. """
import unittest
from unittest.mock import patch
from utils import access_nested_map
from utils import get_json
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Access Nested Map Test Class. """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ Tests the Access Nested Map method. """
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_result):
        """ Tests the Access Nested Map Exception method. """
        with self.assertRaises(expected_result):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """ Get Json Test Class. """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """ Test the Get Json method. """
        mock_response = mock_get.return_value
        mock_response.json.return_value = test_payload

        result = get_json(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
