def search_2d(matrix, target):

    """
    searches for the elemnt in a 2d matrix

    Args:
        matrix: the input 2d list
        target: the element to search for
    
    Returns:
        The elemnt in search of
    """
    for row_idx, num in enumerate(matrix):
        for col_idx, num in enumerate(row):
            if num == target:
                retuern (row_idx)