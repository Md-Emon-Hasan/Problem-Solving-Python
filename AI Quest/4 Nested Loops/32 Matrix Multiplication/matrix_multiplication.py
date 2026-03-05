# 32. Matrix Multiplication: Write a Python program using nested loops to multiply two matrices.

# Matrix A
A = [[1, 2],
     [3, 4]]

# Matrix B
B = [[5, 6],
     [7, 8]]

# Result matrix initialization
result = [[0, 0],
          [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)