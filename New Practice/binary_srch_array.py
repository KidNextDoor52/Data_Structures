def binary_search(arr, target):
    """
    searches for element in a sorted array using binary search

    Args:
        arr: the input array
        target: the element to search for

    Returns:
        the index of the target element if found, -1 otherwise
    """
# starting the search from both sides left and right and working inword
    left, right = 0, len(arr) - 1

#search as long as the left place is smaller than the right 
    while left <= right:
        mid = (left + right) // 2
        #speeding up the process if the middle element is the target
        if arr[mid] == target:
            return mid
        #if the taget isnt the middle it continues to move the right and left search inward
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

array = [1, 3, 5, 7, 9]
target = 5
index = binary_search(array, target)
print(index)