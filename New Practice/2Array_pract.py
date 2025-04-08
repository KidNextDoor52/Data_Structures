import numpy as np

twoDarray = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(twoDarray)
print(twoDarray[2,1])#rememeber index starts at 0

newDarray = np.append(twoDarray,[[13,14,15,16]], axis=0)
print(newDarray)

newDarray2 = np.insert(twoDarray, 3,[[13,14,15,16]], axis=0)
print("This is the second")
print(newDarray2)

print(newDarray2[0,2])

def trav_array(array):
    """
    this fucniton traverses through the two dimensional array
    """
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

trav_array(twoDarray)

def accessElements(array, rowIndex, colIndex):
    """
    this funcion accesses a single element in the two dimensional array
    """
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print("Incorrect index")
    else:
        print(array[rowIndex][colIndex])
    
accessElements(twoDarray, 1, 2,)

