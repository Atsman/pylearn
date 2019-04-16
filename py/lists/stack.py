"""
Implement stack using LinkedList.
"""

from lists.linked_list import LinkedList


class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, data):
        self.ll.prepend(data)

    def pop(self):
        data = self.ll.head.value
        self.ll.delete(0)
        return data
