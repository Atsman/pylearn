def is_balanced(node):
    if not node:
        return 0

    left_height = is_balanced(node.left)
    right_height = is_balanced(node.right)

    if left_height == -1 or right_height == -1 or \
       abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)
