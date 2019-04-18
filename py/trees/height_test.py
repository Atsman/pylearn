import unittest
from trees.binary_tree import BinaryTree
from trees.height import height


class TestHeight(unittest.TestCase):
    def test_test(self):
        self.assertEqual(1, height(BinaryTree()))

        bt = BinaryTree()
        bt.left = BinaryTree()
        bt.left.left = BinaryTree()

        self.assertEqual(3, height(bt))
