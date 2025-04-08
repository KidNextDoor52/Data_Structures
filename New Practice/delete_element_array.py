import numpy as np
import array 

#time complexity of simple deletions are O(n) unless the last element which is constant and O(1)
#space complexity of simple deletions are O(1) because no extra space is needed

arr1 = np.array([1,2,3,4])
arr1_deleted = np.delete(arr1, 2)

print(arr1_deleted)
