def find_ll_head(ll):
    slow_ptr = ll.head
    fast_ptr = ll.head

    is_loop = False
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            is_loop = True
            break

    if is_loop:
        slow_ptr = ll.head
        while slow_ptr != fast_ptr:
            fast_ptr = fast_ptr.next
            slow_ptr = slow_ptr.next
        return slow_ptr
    
    return None
