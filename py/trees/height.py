def height(node, i=0):
    if not node:
        return i

    left_height = height(node.left, i)
    right_height = height(node.right, i)

    return max(left_height, right_height) + 1
