def iter_from(node):
    current_node = node.next
    while current_node:
        yield current_node
        current_node = current_node.next
        

def bruteforce(ll):
    for node in ll.iterator():
        for node2 in iter_from(node):
            if node != node2 and node2.next == node:
                return True
    return False


def hash_table(ll):
    hset = set()
    current_node = ll.head
    while current_node:
        if current_node in hset:
            return True
        hset.add(current_node)
        current_node = current_node.next
    return False


def two_pointers(ll):
    p1 = ll.head
    p2 = ll.head

    while p1 and p2.next:
        p1 = p1.next
        p2 = p2.next.next

        if p1 == p2:
            return True

    return False


def is_cycly_list(ll):
    return bruteforce(ll)
