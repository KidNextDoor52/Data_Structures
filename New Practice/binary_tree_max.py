def find_max_in_tree(root):
    """
    FInds the maximum value in a binary tree

    Args:
        root: The root node of the tree

    Returns:
        the maximum value
    """

    if not root:
        return float('-inf')
    
    left_max = find_max_in_tree(root.left)
    right_max = find_max_in_tree(root.right)

    return max(root.val, left_max, right_max)