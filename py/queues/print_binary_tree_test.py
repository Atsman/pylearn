import unittest
from trees.binary_tree import BinaryTree
from queues.print_binary_tree import print_binary_tree


class TestPrintBinaryTree(unittest.TestCase):
    def test_print(self):
        b1 = BinaryTree()
        b1.value = 28
        
        b2 = BinaryTree()
        b2.value = 0

        b3 = BinaryTree()
        b3.value = 271
        b3.left = b1
        b3.right = b2

        b4 = BinaryTree()
        b4.value = 17

        b5 = BinaryTree()
        b5.value = 3
        b5.left = b4

        b6 = BinaryTree()
        b6.value = 561
        b6.right = b5

        b7 = BinaryTree()
        b7.value = 6
        b7.left = b3
        b7.right = b6

        ####

        b8 = BinaryTree()
        b8.value = 641

        b9 = BinaryTree()
        b9.value = 401
        b9.right = b8

        b10 = BinaryTree()
        b10.value = 257

        b11 = BinaryTree()
        b11.value = 1
        b11.left = b9
        b11.right = b10

        b12 = BinaryTree()
        b12.value = 2
        b12.right = b11

        b13 = BinaryTree()
        b13.value = 28

        b14 = BinaryTree()
        b14.value = 271
        b14.right = b13

        b15 = BinaryTree()
        b15.value = 6
        b15.left = b12
        b15.right = b14

        ####

        b00 = BinaryTree()
        b00.value = 314
        b00.left = b7
        b00.right = b15

        self.assertEqual([314, 6, 6, 271, 561, 2, 271, 28, 0, 3, 1, 28, 17, 401, 257, 641],
                         print_binary_tree(b00))
