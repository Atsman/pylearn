from linked_list import Node


def insert_sorted(ll, value):
    insert_node = Node(value)
    current_node = ll.head

    if not current_node:
        ll.head = insert_node
        return

    while current_node:
        next_node = current_node.next

        if not next_node:
            current_node.next = insert_node 
            return

        if value > current_node.value and value < next_node.value:
            insert_node.next = current_node.next
            current_node.next = insert_node
            return

        current_node = next_node
