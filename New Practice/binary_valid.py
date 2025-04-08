def is_valid_bst(root, min_val=float('-inf'), max_val=float('inf')):
    """

    check if a binary tree is a valid bst

    Args:
        root: the root node
        min_val: the lower bound
        max_val: the upper bound

    Returns:
        True if valid BST, else False

    """
    if not root:
        return True
    
    if not (min_val < root.val < max_val):
        return False
    
    return is_valid_bst(root.left, min_val, root.val) and is_valid_bst(root.right, root.val, max_val)