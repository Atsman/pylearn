"""
Chech whether the given linked list is either terminated or ends in cycle.
"""


def has_cycle_bruteforce(head):
    """
    Check for cycle in LinkedList using bruteforce method.
    For each node in LL, check if next points to current node.
    In that case list has cycle.

    Time complexity O(N^2)
    Space complexity O(1)
    """
    current_node = head
    outer_moves = 0
    while current_node:
        outer_moves += 1
        jnode = current_node.next

        max_inner_moves = outer_moves
        while jnode and max_inner_moves > 0:
            if jnode.next == current_node:
                return True
            jnode = jnode.next
            max_inner_moves -= 1
        current_node = current_node.next
    return False


def has_cycle_hash_table(head):
    """
    Check for cycle in LinkedList using hash table.
    For each node in LL, check if it is in hash table,
    if not add and continue iteration.

    Time compexity O(N)
    Space compexity O(N)
    """
    hset = set()
    current_node = head
    while current_node:
        if current_node in hset:
            return True
        hset.add(current_node)
        current_node = current_node.next
    return False


def has_cycle_two_pointers(head):
    """
    Check for cycle in LinkedList using two pointers:
    slow and fast. Once they enter the loop, they are
    expected to meet, if there is a loop.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    sp = head
    fp = head

    while sp and fp and fp.next:
        sp = sp.next
        fp = fp.next.next

        if sp == fp:
            return True

    return False


def find_cycle_head(head):
    """
    Chech for cycle in LinkedList. If there is a cycle,
    find and return the start node of the loop.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    sp = head
    fp = head

    has_cycle = has_cycle_two_pointers(head)

    if not has_cycle:
        return None

    sp = head
    while sp != fp:
        fp = fp.next
        sp = sp.next

    return sp


def find_cycle_length(head):
    """
    Chech for cycle in LinkedList. If there is a cycle,
    count the length of cycle and return it.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    sp = head
    fp = head

    has_cycle = has_cycle_two_pointers(head)

    if not has_cycle:
        return 0
    
    count = 0
    while sp and fp and fp.next:
        sp = sp.next
        fp = fp.next.next
        count += 1

        if sp == fp:
            break

    return count
