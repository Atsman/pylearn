import unittest
from lists.test_utils import simple_list
from lists.find_nth_from_the_end import find_nth_from_the_end


class TestFindNthFromTheEnd(unittest.TestCase):
    def test_find_nth_from_the_end(self):
        ll = simple_list(10)

        for i in range(0, 10):
            self.assertEqual(9 - i, find_nth_from_the_end(ll.head, i))


if __name__ == '__main__':
    unittest.main()
