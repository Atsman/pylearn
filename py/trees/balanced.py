def is_balanced(node):
    """
    A binary tree is called balanced if for each node
    in the tree, the difference in the height if its
    left and right subtrees is at most one.
    """
    if not node:
        return 0

    left_height = is_balanced(node.left)
    right_height = is_balanced(node.right)

    if left_height == -1 or right_height == -1 or \
       abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)
