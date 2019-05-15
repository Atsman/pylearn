import unittest
from trees.binary_tree import BinaryNode
from queues.print_binary_tree import print_binary_tree


class TestPrintBinaryTree(unittest.TestCase):
    def test_print(self):
        b1 = BinaryNode()
        b1.value = 28
        
        b2 = BinaryNode()
        b2.value = 0

        b3 = BinaryNode()
        b3.value = 271
        b3.left = b1
        b3.right = b2

        b4 = BinaryNode()
        b4.value = 17

        b5 = BinaryNode()
        b5.value = 3
        b5.left = b4

        b6 = BinaryNode()
        b6.value = 561
        b6.right = b5

        b7 = BinaryNode()
        b7.value = 6
        b7.left = b3
        b7.right = b6

        ####

        b8 = BinaryNode()
        b8.value = 641

        b9 = BinaryNode()
        b9.value = 401
        b9.right = b8

        b10 = BinaryNode()
        b10.value = 257

        b11 = BinaryNode()
        b11.value = 1
        b11.left = b9
        b11.right = b10

        b12 = BinaryNode()
        b12.value = 2
        b12.right = b11

        b13 = BinaryNode()
        b13.value = 28

        b14 = BinaryNode()
        b14.value = 271
        b14.right = b13

        b15 = BinaryNode()
        b15.value = 6
        b15.left = b12
        b15.right = b14

        ####

        b00 = BinaryNode()
        b00.value = 314
        b00.left = b7
        b00.right = b15

        self.assertEqual([314, 6, 6, 271, 561, 2, 271, 28, 0, 3, 1, 28, 17, 401, 257, 641],
                         print_binary_tree(b00))
