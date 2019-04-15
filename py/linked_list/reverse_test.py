import unittest
from linked_list import from_array_list
from reverse import reverse_ll, reverse_recursive_ll


methods = [reverse_ll, reverse_recursive_ll]


class TestReverseLinkedList(unittest.TestCase):
    def test_reverse(self):
        for method in methods:
            ll = from_array_list([1, 2, 3, 4])
            self.assertEqual([4, 3, 2, 1], method(ll).to_list())


if __name__ == '__main__':
    unittest.main()
