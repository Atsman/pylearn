import unittest
from strings.run_length_encoding import run_length_encoding


class TestRunLengthEncoding(unittest.TestCase):
    def test_encoding(self):
        self.assertEqual("4a1b3c2a", run_length_encoding("aaaabcccaa"))
