import numpy as np
my_array = np.array([[1, 2, 3], [4, 5, 6]])
# print(my_array)
# def accessTwoDimensionalArray(array, row, column):
#     if row >= len(array) or column >= len(array[0]):
#         return "Incorrect index"
#     return array[row][column]
# print(accessTwoDimensionalArray(my_array, 1, 2))

# traversal of a 2D array
def traverseTwoDimensionalArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseTwoDimensionalArray(my_array)

# Time complexity of accessing an element in a 2D array is O(1) and for traversing a 2D array is O(m*n) where m is the number of rows and n is the number of columns in the 2D array.
# Space complexity of accessing an element in a 2D array is O(1) and for traversing a 2D array is O(1).
# The space complexity of a 2D array is O(m*n) where m is the number of rows and n is the number of columns in the 2D array.

