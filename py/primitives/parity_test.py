import unittest
from primitives.parity import parity_bruteforce, parity_xor


class TestParity(unittest.TestCase):
    def test_parity(self):
        methods = [parity_bruteforce, parity_xor]
        for method in methods:
            self.assertEqual(1, method(1))
            self.assertEqual(1, method(2))
            self.assertEqual(0, method(3))
            self.assertEqual(0, method(5))
