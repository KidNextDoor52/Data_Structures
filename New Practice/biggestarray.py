
def findBiggestArray(sampleArray):
    biggestNumber = sampleArray[0] # O(1) - the constant variable
    for index in range(1, len(sampleArray)): # O(n) - simple "for" loop
        if sampleArray[index] > biggestNumber: # O(1) # constant 
            biggestNumber = sampleArray[index] # O(1) - constant 
        print(biggestNumber) # after adding you get O(1) + O(1) + O(n) = O(n) time complexity

findBiggestArray([1, 34, 53, 34, 54, 76, 345, 345, 23, 45, 646, 45, 235])