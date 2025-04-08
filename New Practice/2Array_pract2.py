import numpy as np

twoDarray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

#def search_2d_array(array, target):
#    for i in range(len(array)):
#        for j in range(len(array[0])):
#            if array[i][j] == target:
#                return "the target is at index "+str(i)+","+str(j)
#    return 'element is not in array'


#print(search_2d_array(twoDarray, 13))

deleted_array_element = np.delete(twoDarray, 2, axis=0)# the 2 deletes the 2 index row, if you change 0 it deletes column
print(deleted_array_element)
#O(mn) complexity for simple 2d array function

