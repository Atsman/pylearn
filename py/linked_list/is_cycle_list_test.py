import unittest 
from linked_list import LinkedList, from_array_list
from is_cycle_list import bruteforce, two_pointers, hash_table


def create_cycle_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.last().next = ll.head
    return ll


def create_list():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    return ll


methods = [bruteforce, hash_table, two_pointers]


class TestIsCycleList(unittest.TestCase):
    def test_is_cycle_list(self):
        for method in methods:
            ll = create_list()
            self.assertFalse(method(ll), method.__name__) 

            cll = create_cycle_list()
            self.assertTrue(method(cll), method.__name__)


if __name__ == '__main__':
    unittest.main()
