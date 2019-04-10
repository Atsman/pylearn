import unittest
from linked_list import LinkedList, Node

class TestLinkedList(unittest.TestCase):
    def test_constructor(self):
        ll = LinkedList()
        self.assertEqual(ll.head, None)

    def test_to_list(self):
        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = Node(2)
        ll.head.next.next = Node(3)
        self.assertEqual([1, 2, 3], ll.to_list())

    def test_insert(self):
        ll = LinkedList()
        ll.insert(1, 0)
        self.assertEqual(1, ll.head.value)
        ll.insert(2, 1)
        self.assertEqual(2, ll.head.next.value)
        ll.insert(3, 2)
        self.assertEqual(3, ll.head.next.next.value)

    def test_prepend(self):
        ll = LinkedList()
        ll.prepend(1)
        self.assertEqual([1], ll.to_list())
        ll.prepend(2)
        self.assertEqual([2, 1], ll.to_list())
        ll.prepend(3)
        self.assertEqual([3, 2, 1], ll.to_list())

    def test_append(self):
        ll = LinkedList()
        ll.append(1)
        self.assertEqual([1], ll.to_list())
        ll.append(2)
        self.assertEqual([1, 2], ll.to_list())

    def test_last(self):
        ll = LinkedList()
        ll.head = Node(1)
        ll.head.next = Node(2)
        ll.head.next.next = Node(3)
        self.assertEqual(3, ll.length())

    def test_get(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)

        self.assertEqual(1, ll.get(0).value)
        self.assertEqual(2, ll.get(1).value)
        self.assertEqual(3, ll.get(2).value)
        self.assertEqual(None, ll.get(3))

    def test_delete(self):
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        ll.append(4)

        ll.delete(0)
        self.assertEqual([2, 3, 4], ll.to_list())

        ll.delete(1)
        self.assertEqual([2, 4], ll.to_list())

        ll.delete(1)
        self.assertEqual([2], ll.to_list())

        ll.delete(0)
        self.assertEqual([], ll.to_list())


if __name__ == '__main__':
    unittest.main()
