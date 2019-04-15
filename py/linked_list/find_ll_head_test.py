import unittest
from find_ll_head import find_ll_head
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


class TestFindLLHead(unittest.TestCase):
    def test_find_ll_head(self):
        ll = create_cycle_list()

        self.assertEqual(ll.head, find_ll_head(ll))


if __name__ == '__main__':
    unittest.main()
