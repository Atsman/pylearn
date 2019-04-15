import unittest
from linked_list import LinkedList
from nth_node_from_end import nth_node_from_end


class TestNthFromEnd(unittest.TestCase):
    def test_nth_from_end(self):
        ll = LinkedList()

        for i in range(0, 10):
            ll.append(i)

        for i in range(1, 10):
            print(i, nth_node_from_end(ll, i))


if __name__ == '__main__':
    unittest.main()
