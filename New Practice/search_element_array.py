import array
import numpy as np
"""
creating a function 'linear_search' to search inputed array for a target element
vars:
    arr1 - the sample array
    np_arr1 - converted array
args:
    arr - the input array
    target - the element in search of
"""
#create the array arr1 then convert it in to a np.array for flexibility
arr1 = array.array('i', [1,2,3,4,5])
np_arr1 = np.array(arr1)


def linear_search(arr, target):
    for i in range(len(arr)):#O(n^2)
        if arr[i] == target:#O(1)
            return i
    return -1
    
print(linear_search(arr1, 6))
#space complexity O(1) because additional memory isnt required for this
#time complexity O(1) because len and range fuction cause its constant. Called once