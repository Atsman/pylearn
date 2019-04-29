from trees.binary_tree import BinaryTree
from queues.queue import Queue


def print_binary_tree(tree):
    """
    Given the root of binary tree, converts it 
    to array, so that all elements are in order
    of their level.

    Time complexity: O(N)
    Space complexity: O(N)
    """
    queue = Queue()
    queue.enqueue(tree)
    result = []
    while not queue.empty():
        node = queue.dequeue()

        if node.left:
            queue.enqueue(node.left)

        if node.right:
            queue.enqueue(node.right)

        result.append(node.value)
    return result
