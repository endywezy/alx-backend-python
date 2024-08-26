#!/usr/bin/env python3
"""A module for testing GithubOrgClient."""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""

    @parameterized.expand([
        ('google', {'org': 'google'}),
        ('abc', {'org': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_payload: dict,
                 mock_get_json: Mock) -> None:
        """Test that GithubOrgClient.org returns the correct value."""
        mock_get_json.return_value = expected_payload
        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )


if __name__ == "__main__":
    unittest.main()
