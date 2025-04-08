def binary_search(arr, target):
    """
    searches for an element in a array using binary search

    Args:
        arr: input array
        target: the element to search

    Return:
        Returns the index of the element if found, -1 otherwise

    """

    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        
    return -1
