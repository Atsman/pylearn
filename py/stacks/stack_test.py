import unittest
from stacks.stack import Stack


class TestMaxStack(unittest.TestCase):
    def test_max(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(999)
        stack.push(222)
        stack.push(111)

        self.assertEqual(999, stack.max())

        stack.pop()
        stack.pop()
        stack.pop()

        self.assertEqual(2, stack.max())
