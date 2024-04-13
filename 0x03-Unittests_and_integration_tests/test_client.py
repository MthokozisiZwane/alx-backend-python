#!/usr/bin/env python3


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for the GithubOrgClient class."""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value.

        Parameters:
            org_name (str): The name of the GitHub organization.
            mock_get_json (MagicMock): Mock object for get_json function.
        """
        client = GithubOrgClient(org_name)
        expected_url = f"https://api.github.com/orgs/{org_name}"

        # Call org() method
        client.org()

        # Assert get_json is called once with the expected argument
        mock_get_json.assert_called_once_with(expected_url)


if __name__ == "__main__":
    unittest.main()
