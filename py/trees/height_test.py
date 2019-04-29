import unittest
from trees.binary_tree import BinaryNode
from trees.height import height


class TestHeight(unittest.TestCase):
    def test_test(self):
        self.assertEqual(1, height(BinaryNode()))

        bt = BinaryNode()
        bt.left = BinaryNode()
        bt.left.left = BinaryNode()
        bt.right = BinaryNode()
        bt.right.right = BinaryNode()
        bt.right.right.right = BinaryNode()

        self.assertEqual(4, height(bt))
