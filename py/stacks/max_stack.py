from lists.linked_list import LinkedList


class Stack:
    """
    Stack implementation using linked list which
    supports max operation.

    Implemented using two linked lists. One for elements
    themselfs and one for current max value.

    Time complexity: O(1)
    Space complexity: O(N) + O(N) for max value.
    """
    def __init__(self):
        self._main_stack = LinkedList()
        self._max_stack = LinkedList()
        self._map = {}

    def peek(self):
        """
        Takes object from the top of this stack
        without removing it from the stack.
        """
        return self._main_stack.head.value

    def pop(self):
        """
        Removes object from the top of this stack
        and returns that object.
        """
        head = self._main_stack.head.value
        self._main_stack.delete(0)
        self._max_stack.delete(0)

        return head

    def push(self, item):
        """
        Pushes an item onto the top of this stack.
        """
        if not self._max_stack.head or self._max_stack.head.value < item:
            self._max_stack.prepend(item)
        else:
            self._max_stack.prepend(self._max_stack.head.value)

        self._main_stack.prepend(item)

    def max(self):
        return self._max_stack.head.value
