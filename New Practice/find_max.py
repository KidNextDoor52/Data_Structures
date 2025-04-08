#def find_max(arr):
#    """ Finds the max array for FLOATING NUMBERS
#        args:
#            arr: the input array
#        returns:
#            The maximum in the array, or None if the array is empty
#    """
#    #if there is nothin in the array then it return None
#    if not arr:
#        return None
#    #starts the array at the first element
#    max_val = arr[0]
#    #creates the variable max_val for the max of "num" and returns it
#    for num in arr:
#        max_val = max(max_val, num)
#    return max_val
#
#array = [1.2, 5.7, 2.4, 8.9, 3.3]
#
#print(find_max(array))


def find_max(arr):
    """This function finds the max of an array that includes duplicates

    Args:
        arr: input array
    Returns:
        The max in an array or None if the array is empty
    """
    