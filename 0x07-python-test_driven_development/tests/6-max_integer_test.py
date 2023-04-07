#!/usr/bin/python3

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Unit tests for max_integer function.
    """

    def test_empty_list(self):
        """
        Test that an empty list returns None.
        """
        self.assertIsNone(max_integer([]))

    def test_single_item_list(self):
        """
        Test that a list with one item returns that item.
        """
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_items_list(self):
        """
        Test that a list with multiple items returns the maximum value.
        """
        self.assertEqual(max_integer([1, 2, 3]), 3)
        self.assertEqual(max_integer([3, 2, 1]), 3)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([-3, -2, -1]), -1)
        self.assertEqual(max_integer([1, 1, 1]), 1)

    def test_floats(self):
        """
        Test that a list of floats returns the maximum value.
        """
        self.assertEqual(max_integer([1.53, 6.33, -9.123, 15.2, 6.0]), 15.2)

    def test_strings(self):
        """
        Test that a list of strings raises TypeError.
        """
        with self.assertRaises(TypeError):
            max_integer(["abc", "def", "ghi"])

    def test_mixed_types(self):
        """
        Test that a list with mixed types raises TypeError.
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, "abc", 3.14, -5])

    def test_no_args(self):
        """
        Test that max_integer raises TypeError when called without arguments.
        """
        with self.assertRaises(TypeError):
            max_integer()
