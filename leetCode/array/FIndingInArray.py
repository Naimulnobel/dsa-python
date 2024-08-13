import numpy as np

my_array = np.array([1, 2, 3, 4, 5])
def linearSearch(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i
    return "Element not found"
print(linearSearch(my_array, 5))
print(linearSearch(my_array, 6))