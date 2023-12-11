"""Example of unit tests."""

import arithmetic
from unittest import TestCase

class AdditionTestCase(TestCase):
    """Example of unit tests."""
    
    def test_adder(self):
        assert arithmetic.adder(2, 3) == 5
        
    def test_adder_2(self):
        # instead of assert arithmetic.adder(2, 2) == 4
        self.assertEqual(arithmetic.adder(2, 2), 4)
        self.assertEqual(arithmetic.adder(40, 50), 90)
        self.assertEqual(arithmetic.adder(-2, -4), -6)
