import unittest
from trees.binary_tree import BinaryTree
from trees.height import height


class TestHeight(unittest.TestCase):
    def test_test(self):
        self.assertEqual(1, height(BinaryTree()))

        bt = BinaryTree()
        bt.left = BinaryTree()
        bt.left.left = BinaryTree()
        bt.right = BinaryTree()
        bt.right.right = BinaryTree()
        bt.right.right.right = BinaryTree()

        self.assertEqual(4, height(bt))
