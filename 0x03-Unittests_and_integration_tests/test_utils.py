#!/usr/bin/env python3
"""A module for testing the access_nested_map function in utils."""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Tests for the access_nested_map function."""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map: dict, path: tuple, expected: int) -> None:
        """
        Test access_nested_map with various inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys to traverse in the nested map.
            expected (int): The expected result from the function.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: dict, path: tuple) -> None:
        """
        Test that access_nested_map raises a KeyError for invalid paths.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys to traverse in the nested map.
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        
        # Ensure the exception message matches the missing key in the path
        self.assertEqual(str(context.exception), f"'{path[-1]}'")


if __name__ == "__main__":
    unittest.main()
