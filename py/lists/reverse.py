"""
Reverse single linked list.
There are two ways to solve that problem.
"""


def reverse_iterative(head):
    """
    Reverse single linked list using iterative method.

    Time complexity: O(N)
    Space complexity: O(1)
    """
    previous_node = None
    current_node = head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    return previous_node


def reverse_recursive(head):
    """
    Reverse single linked list using recursive method.

    Time complexity: O(N)
    Space complexity: O(N) (for stack)
    """
    if not head or not head.next:
        return head

    second = head.next
    head.next = None
    reversedRest = reverse_recursive(second)  # reverse from second
    second.next = head  # join lists

    return reversedRest
