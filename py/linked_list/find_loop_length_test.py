import unittest
from find_loop_length import find_loop_length
from linked_list import LinkedList


def create_cycle_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.last().next = ll.head
    return ll


class TestFindLoopLength(unittest.TestCase):
    def test_find_loop_lengt(self):
        ll = create_cycle_list()
        self.assertEqual(5, find_loop_length(ll))

        ll = LinkedList()
        self.assertEqual(0, find_loop_length(ll))


if __name__ == '__main__':
    unittest.main()
