import unittest
from lists.linked_list import LinkedList, from_array_list
from lists.insert_sorted import insert_sorted


class TestInsertSorted(unittest.TestCase):
    def test_insertsorted(self):
        ll = from_array_list([1, 2, 3, 5, 6, 7])
        insert_sorted(ll, 4)
        self.assertEqual([1, 2, 3, 4, 5, 6, 7], ll.to_list())

        ll = from_array_list([1, 2, 3])
        insert_sorted(ll, 4)
        self.assertEqual([1, 2, 3, 4], ll.to_list())

        ll = LinkedList()
        insert_sorted(ll, 1)
        self.assertEqual([1], ll.to_list())


if __name__ == '__main__':
    unittest.main()
