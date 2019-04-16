import unittest 
from lists.linked_list import LinkedList
from lists.test_utils import simple_list, cycle_list, random_cycle_list
from lists.has_cycle import has_cycle_bruteforce, has_cycle_hash_table, \
    has_cycle_two_pointers, find_cycle_head, find_cycle_length


LIST_SIZE = 10


class TestHasCycleList(unittest.TestCase):
    def setUp(self):
        self.methods = [has_cycle_bruteforce, has_cycle_hash_table,
                        has_cycle_two_pointers]

    def test_has_cycle_list(self):
        for method in self.methods:
            ll = LinkedList()
            self.assertFalse(method(ll.head), method.__name__)

            ll = simple_list(LIST_SIZE)
            self.assertFalse(method(ll.head), method.__name__) 

            cll = cycle_list(LIST_SIZE)
            self.assertTrue(method(cll.head), method.__name__)

            rcll = random_cycle_list(LIST_SIZE)
            self.assertTrue(method(rcll.head), method.__name__)


class TestFindCycleHead(unittest.TestCase):
    def test_find_ll_head(self):
        ll = cycle_list(LIST_SIZE)
        self.assertEqual(ll.head, find_cycle_head(ll.head))


class TestFindLoopLength(unittest.TestCase):
    def test_find_loop_lengt(self):
        ll = cycle_list(LIST_SIZE)
        self.assertEqual(LIST_SIZE, find_cycle_length(ll.head))

        ll = LinkedList()
        self.assertEqual(0, find_cycle_length(ll.head))


if __name__ == '__main__':
    unittest.main()
