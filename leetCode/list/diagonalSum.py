def diagonal_sum(matrix):
    return sum(matrix[i][i] for i in range(len(matrix)))


print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

#print peramid matrix
def print_peramid(n):
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print("\r")


print_peramid(5)