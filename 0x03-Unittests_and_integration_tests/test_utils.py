#!/usr/bin/env python3
""" Unittest Task."""
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ Parameterize a unit test."""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
            ) -> None:
        """ Tests the test access nested map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
                self,
                nested_map: Dict,
                path: Tuple[str],
                exception: Exception
            ) -> None:
        """ Tests access nested map exception."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
