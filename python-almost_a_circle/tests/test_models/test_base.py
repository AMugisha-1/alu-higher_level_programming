#!/usr/bin/python3
"""
Unit tests for the Base class.
"""

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_no_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_with_id(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_mixed_ids(self):
        b1 = Base()
        b2 = Base(99)
        b3 = Base()
        self.assertEqual(b1.id + 1, b3.id)

if __name__ == "__main__":
    unittest.main()
