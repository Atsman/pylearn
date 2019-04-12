import unittest
from linked_list import LinkedList
from tasks import nth_node_from_end


class TestTasks(unittest.TestCase):
    def test_nth_from_end(self):
        ll = LinkedList()

        for i in range(0, 10):
            ll.append(i)

        for i in range(1, 10):
            print(i, nth_node_from_end(ll, i))


if __name__ == '__main__':
    unittest.main()
