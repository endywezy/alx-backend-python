#!/usr/bin/env python3
"""A module for testing utility functions."""

import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple,
                               expected: object) -> None:
        """Test access_nested_map with various inputs."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict,
                                         path: tuple) -> None:
        """Test that access_nested_map raises a KeyError for invalid paths."""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), repr(path[-1]))


class TestGetJson(unittest.TestCase):
    """Tests for the get_json function."""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, test_payload: dict) -> None:
        """Test get_json with mocked HTTP response."""
        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = Mock(json=lambda: test_payload)

            response = get_json(test_url)
            self.assertEqual(response, test_payload)

            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Tests for the memoize decorator."""

    def test_memoize(self) -> None:
        """Test memoize to ensure method is only called once."""
        class TestClass:
            """Class to test memoization."""

            def a_method(self) -> int:
                """Return a fixed integer."""
                return 42

            @memoize
            def a_property(self) -> int:
                """Return the result of a_method."""
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_m:
            test_instance = TestClass()
            self.assertEqual(test_instance.a_property, 42)
            self.assertEqual(test_instance.a_property, 42)
            mock_m.assert_called_once()


if __name__ == "__main__":
    unittest.main()
