import unittest
from arrays.rearrange import rearrange


class TestRearrange(unittest.TestCase):
    def test_rearrange(self):
        arr = [1, 7, 6, 4, 3, 8, 9, 4, 2]
        rearrange(arr, 3)
        self.assertEqual([1, 2, 3, 4, 4, 9, 8, 6, 7], arr)

        arr = [5, 4, 3, 2, 1]
        rearrange(arr, 2)
        self.assertEqual([1, 2, 3, 4, 5], arr)
