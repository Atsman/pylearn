"""
LinkedList test utils. Functions for generating lists.
"""

import random
from lists.linked_list import LinkedList


def simple_list(n):
    """
    Generates simple linked lists with numbers from 0 to n.

    Time complexity: O(n)
    Space complexity: O(n)
    """
    ll = LinkedList()
    for i in range(n - 1, -1, -1):
        ll.prepend(i)
    return ll


def cycle_list(n):
    """
    Generates cycle list with numbers from 0 to n.
    Last node points to head.
    """
    ll = simple_list(n)

    last = ll.last()
    last.next = ll.head

    return ll


def random_cycle_list(n):
    """
    Generates cycle list with numbers from 0 to n.
    Last node points to random node.
    """
    ll = simple_list(n)

    last = ll.last()
    random_node = ll.get(random.randint(0, n-1))
    last.next = random_node

    return ll
