def height(tree, i=0):
    if not tree:
        return i

    left_height = height(tree.left, i)
    right_height = height(tree.right, i)

    return max(left_height, right_height) + 1
