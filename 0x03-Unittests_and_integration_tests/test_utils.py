#!/usr/bin/env python3
""" Unittest Task."""
from parameterized import parameterized
from typing import Dict, Tuple, Union
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json, memoize


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


class TestGetJson(unittest.TestCase):
    """ Mock HTTP calls."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(
                self,
                test_url: str,
                test_payload: Dict
            ) -> None:
        """ Tests get json function."""
        attrs = {'json.return_value': test_payload}
        with patch('requests.get', return_value=Mock(**attrs)) as get_r:
            self.assertEqual(get_json(test_url), test_payload)
            get_r.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Parameterize and Patch."""
    def test_memoize(self) -> None:
        """ Tests memorize function."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(
                    TestClass,
                    "a_method",
                    return_value=lambda: 42
                ) as memorize_function:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)

            memorize_function.assert_called_once()
