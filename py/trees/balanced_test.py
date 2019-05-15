import unittest
from trees.binary_tree import BinaryNode
from trees.balanced import is_balanced


class TestBalanced(unittest.TestCase):
    def test_single_node(self):
        bt = BinaryNode()
        self.assertTrue(bt)

    def test_balanced(self):
        bt = BinaryNode()
        bt.left = BinaryNode()
        bt.right = BinaryNode()
        self.assertTrue(bt)

    def test_not_balanced(self):
        bt = BinaryNode()
        bt.left = BinaryNode()
        bt.left.left = BinaryNode()
        self.assertFalse(is_balanced(bt))

    def test_not_balanced2(self):
        bt = BinaryNode()
        bt.left = BinaryNode()
        bt.left.left = BinaryNode()
        bt.right = BinaryNode()
        bt.right.right = BinaryNode()
        bt.right.right.right = BinaryNode()

        self.assertFalse(is_balanced(bt))
