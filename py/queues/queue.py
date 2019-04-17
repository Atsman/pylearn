from lists.linked_list import Node


class Queue:
    """
    Queue implementation using linked list's Node.
    """
    def __init__(self):
        self._head = None
        self._tail = None

    def empty(self):
        return not self._head

    def enqueue(self, item):
        node = Node(item)

        if not self._head:
            self._head = node
            return

        if not self._tail:
            self._tail = node
            self._head.next = self._tail
            return

        self._tail.next = node
        self._tail = node

    def dequeue(self):
        if not self._head:
            raise "No items"

        item = self._head
        self._head = self._head.next
        return item.value
