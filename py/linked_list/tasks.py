def nth_node_from_end(ll, n):
    head = ll.head
    count = 0
    ptr = head

    while head:
        count += 1
        if count == n:
            ptr = head

        if count > n:
            ptr = ptr.next

        head = head.next

    return ptr.value

