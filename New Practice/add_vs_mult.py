def print_items(a,b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)
#this is a add O(A + B) because its a do this finish then do that 


def print_items(a,b):
    for i in range(a):
        for j in range(b):
            print(i, j)
#this is a multiply becaue its shows O(A*B) beacause its a do this for each time you do that