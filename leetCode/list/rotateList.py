def rotate(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i):
            print(i,j)
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))