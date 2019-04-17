from trees.binary_tree import BinaryTree
from queues.queue import Queue


def print_binary_tree(tree):
    """
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
