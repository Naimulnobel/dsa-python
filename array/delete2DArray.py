import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6]])
print(my_array)
# delete a row from a 2D array
new_array = np.delete(my_array, 1, axis=0)
print(new_array)
# delete a column from a 2D array
new_array1 = np.delete(my_array, 1, axis=1)
print(new_array1)