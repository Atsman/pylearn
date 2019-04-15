def find_loop_length(ll):
    slow_ptr = ll.head
    fast_ptr = ll.head

    is_loop = False
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

        if slow_ptr == fast_ptr:
            is_loop = True
            break

    if not is_loop:
        return 0
    
    count = 0
    while slow_ptr and fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
        count += 1

        if slow_ptr == fast_ptr:
            break

    return count
