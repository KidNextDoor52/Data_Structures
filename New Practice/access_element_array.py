import numpy as np
import array 

arr1 = array.array('i', [1,2,3,4,5,6])

arr_np = np.array(arr1)

def find_element(array, index):
    if index >= len(array):
        print('There is not any element in index')
    else:
        print(array[index])

find_element(arr1, 6)


