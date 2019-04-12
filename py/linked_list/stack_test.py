import unittest
from stack import Stack


class TestStack(unittest.TestCase):
    def test_constructor(self):
        stack = Stack()
        self.assertIsNotNone(stack)

    def test_operations(self):
        stack = Stack()

        stack.push(1)
        stack.push(2)
        stack.push(3)

        self.assertEqual(3, stack.pop())
        self.assertEqual(2, stack.pop())
        self.assertEqual(1, stack.pop())


if __name__ == '__main__':
    unittest.main()
