import numpy as np
import array

arr1 = array.array('i', [1,2,3,4])
arr2 = array.array('f', [1.3, 1.5, 1.6])
arr1_np = np.array(arr1)
arr2_np = np.array(arr2)

#print(arr1)

#arr1.insert(2,9)
#print(arr1)

def trav_array(array):
    for i in array:
        print(i)

trav_array(arr2_np)
