#!/usr/bin/env python3


import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


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

    @patch("client.get_json", return_value={
        "repos_url": "https://api.github.com/orgs/test_org/repos"
    })
    def test_public_repos_url(self, mock_get_json):
        """Test the _public_repos_url property of GithubOrgClient.

        Parameters:
            mock_get_json (MagicMock): Mock object for the get_json function.
        """
        client = GithubOrgClient("test_org")

        # Assert _public_repos_url returns the expected URL
        expected_url = "https://api.github.com/orgs/test_org/repos"
        self.assertEqual(client._public_repos_url, expected_url)


    @patch("client.get_json", return_value=[{"name": "repo1"}, {"name": "repo2"}])
    @patch.object(GithubOrgClient, '_public_repos_url', return_value="https://api.github.com/orgs/test_org/repos")
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test the public_repos method of GithubOrgClient.

        Parameters:
            mock_repos_url (MagicMock): Mock object for the _public_repos_url property.
            mock_get_json (MagicMock): Mock object for the get_json function.
        """
        client = GithubOrgClient("test_org")

        # Call public_repos() method
        repos = client.public_repos()

        # Assert the list of repos is what is expected from the chosen payload
        self.assertEqual(repos, ["repo1", "repo2"])

        # Assert that the mocked property and the mocked get_json were called once
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license method of GithubOrgClient.

        Parameters:
            repo (dict): Repository dictionary containing license information.
            license_key (str): The license key to check.
            expected (bool): The expected result of has_license.
        """
        client = GithubOrgClient("test_org")

        # Call has_license() method
        result = client.has_license(repo, license_key)

        # Assert the returned value matches the expected value
        self.assertEqual(result, expected)

@parameterized_class(("org_payload", "repos_payload", "expected_repos", "apache2_repos"), [
    (org_payload, repos_payload, expected_repos, apache2_repos),
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for the GithubOrgClient class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        cls.get_patcher = patch("client.requests.get")
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos method."""
        # Set up the mock response
        self.mock_get.return_value.json.side_effect = [self.org_payload, self.repos_payload]

        # Create the GithubOrgClient instance
        client = GithubOrgClient("test_org")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert the result matches the expected repos
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos method with license argument."""
        # Set up the mock response
        self.mock_get.return_value.json.side_effect = [self.org_payload, self.repos_payload]

        # Create the GithubOrgClient instance
        client = GithubOrgClient("test_org")

        # Call the public_repos method with license argument
        repos = client.public_repos(license="apache-2.0")

        # Assert the result matches the expected repos with Apache 2.0 license
        self.assertEqual(repos, self.apache2_repos)

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        cls.get_patcher = patch("client.requests.get")
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos method."""
        # Set up the mock response
        self.mock_get.return_value.json.side_effect = [org_payload, repos_payload]

        # Create the GithubOrgClient instance
        client = GithubOrgClient("test_org")

        # Call the public_repos method
        repos = client.public_repos()

        # Assert the result matches the expected repos
        self.assertEqual(repos, expected_repos)

    def test_public_repos_with_license(self):
        """Test GithubOrgClient.public_repos method with license argument."""
        # Set up the mock response
        self.mock_get.return_value.json.side_effect = [org_payload, repos_payload]

        # Create the GithubOrgClient instance
        client = GithubOrgClient("test_org")

        # Call the public_repos method with license argument
        repos = client.public_repos(license="apache-2.0")

        # Assert the result matches the expected repos with Apache 2.0 license
        self.assertEqual(repos, apache2_repos)


if __name__ == "__main__":
    unittest.main()
