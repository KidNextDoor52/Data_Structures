def reverse_array(arr):
    """ reverse array in place

    args:
        arr: input array

    returns:
        reversed array
    """
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr
array = [1, 12, 34, 42, 12, 4, -1, -2]

reversed_array = reverse_array(array)

print(reverse_array(array))
