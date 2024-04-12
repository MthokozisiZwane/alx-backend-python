#!/usr/bin/env python3


import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, MagicMock, PropertyMock
from utils import get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for the access_nested_map function."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Test access_nested_map with valid inputs."""
        result = access_nested_map(nested_map, path)

        # Check the result
        self.assertEqual(result, expected_result)

    @parameterized.expand([
        ({}, ("a",), KeyError, "'a'"),
        ({"a": 1}, ("a", "b"), KeyError, "'b'")
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception, expected_message):
        """Test access_nested_map with invalid inputs, expecting exceptions."""
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """Test case for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json function with mocked HTTP calls."""

        mock_response = MagicMock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()
