def find_nth_from_the_end(head, n):
    """
    find_nth_from_the_end returns nth value
    from the end of the linked list if it exists,
    or None if not.

    Time complexity: O(n)
    Space complexituy: O(1)
    """
    count = 0
    ptr = None

    current_node = head
    while current_node:
        if count >= n:
            if not ptr:
                ptr = head
            else:
                ptr = ptr.next

        count += 1
        current_node = current_node.next

    if ptr:
        return ptr.value

    return None
