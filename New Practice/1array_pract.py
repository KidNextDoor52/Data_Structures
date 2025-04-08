import numpy as np
import array
# 1. creat an array and traverse



arr1 = array.array('i', [1,2,3,4,5])
np_array = np.array(arr1)

def traverse_array(array):
    for i in array:
        print(i)

traverse_array(np_array)

# 2. Access individual elements through indexes
print("Step 2")
print(np_array[2])
# 3. Append any value to the array using append() method
print("step 3")
arr1.append(4)
print(arr1)
# 4. Insert value in any array using insert() method
print("step 4")
np_inserted = np.insert(np_array, 5, 6)
print(np_inserted)
# 5. Extend python array using extend() method
print("step 5")
arr2 = np.append(np_array, [6,7,8])
print(arr2)

#arr3 = array.array('i', [6,7,8])
#arr4 = array.copy(arr3)
#arr4.extend(arr3)
#print(arr4)


# 6. Add items from list into array using fromlist() method
print("Step 6")

tempList = [20, 21, 22]
"""arr2 = np.append(arr2, tempList) #add temp list items using append method

arr2 = np.concatenate((arr2, np.array(tempList))) #add temp list items using concatenate method

print(arr2)
"""
# 7. Remove any array elemnt using rmeove() method
print("Step 7")

tempList = np.delete(tempList, [1])

print(tempList)

# 8. Remove last array elemnt using pop() method
print("step 8")

arr2 = np.array([1,2,3,4,5,6,7,8,9,10])

arr2 = np.delete(arr2, -1)


print(arr2)

# 9. Fetch any elemnt through its index using index() method
print("step 9")
print(arr2[8])
# 10. Reverse a python array using reverse() method
print("step 10")
print(arr2[::-1])
# 11. Get array buffer information through buffer_info() method
print("step 11")
print(arr2.data)
# 12. Check for number of occurences of an element using count() method
print("step 12")
print((arr2 == 7).sum())
# 13. Convert array to string using tostring() method
print("step 13")
arr_bytes = arr2.tobytes()
arr_str = np.array2string(arr2)

print(arr_str)
print(type(arr_str))


# 14. Convert array to a python list with same elements using tolist()
print("step 14")

arr_list = arr2.tolist()

print(arr_list)

# 15. Append a string to char array using fromstring() method

char_arr = np.array(list("Hello "), dtype='U1')
char_arr = np.append(char_arr, list("World"))
print(char_arr)


# 16. Slice Elements from an array

print(arr2)
print(arr2[2:8])


