def tree_height(root):
    """
    computes height(depth) of a binary tree

    Args:
        root: the root node of the tree
    
    Returns:
        The height of the tree
    """

    if not root:
        return 0
    return 1 + max(tree_height(root.left), tree_height(root.right))