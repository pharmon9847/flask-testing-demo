from unittest import TestCase
from algorithms import reverse_str, is_palindrome, factorial

class AlgorithmsTestCase(TestCase):
    def test_reverse(self):
        self.assertEqual(reverse_str('hello'), 'olleh')
        self.assertEqual(reverse_str('Apple'), 'elppA')