import unittest
from lists.linked_list import LinkedList, from_array_list
from lists.merge_sorted import merge_sorted


class TestMergeSorted(unittest.TestCase):
    def test_merge_sorted(self):
        ll1 = from_array_list([1, 3, 5, 7, 9])
        ll2 = from_array_list([1, 4, 6, 8])

        head = merge_sorted(ll1.head, ll2.head)
        ll = LinkedList()
        ll.head = head

        self.assertEqual([1, 1, 3, 4, 5, 6, 7, 8, 9], ll.to_list())
