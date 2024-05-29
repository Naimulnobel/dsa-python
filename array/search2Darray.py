import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6]])
def search2Darray(array,element):
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]==element:
                return i,j
    return "Element not found"
print(search2Darray(my_array, 5))
print(search2Darray(my_array, 6))