def reverse_ll(ll):
    previous_node = None
    current_node = ll.head

    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        temp = current_node
        current_node = next_node

    ll.head = temp
    return ll


def reverse_iter_ll(head):
    if not head:
        return head

    if not head.next:
        return head

    second = head.next
    second.next = None

    reversed_list = reverse_recursive_ll(second)
    second.next = reversed_list

    return reversed_list


def reverse_recursive_ll(ll):
    ll.head = reverse_iter_ll(ll.head)
    return ll
