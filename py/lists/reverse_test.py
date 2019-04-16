import unittest
from lists.linked_list import from_array_list
from lists.reverse import reverse_iterative, reverse_recursive


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse(self):
        methods = [reverse_iterative, reverse_recursive]

        for method in methods:
            ll1 = from_array_list([])
            ll1.head = method(ll1.head)
            self.assertEqual([], ll1.to_list(), method.__name__)

            ll2 = from_array_list([1])
            ll2.head = method(ll2.head)
            self.assertEqual([1], ll2.to_list(), method.__name__)

            ll3 = from_array_list([1, 2])
            ll3.head = method(ll3.head)
            self.assertEqual([2, 1], ll3.to_list(), method.__name__)

            ll4 = from_array_list([1, 2, 3])
            ll4.head = method(ll4.head)
            self.assertEqual([3, 2, 1], ll4.to_list(), method.__name__)


if __name__ == '__main__':
    unittest.main()
