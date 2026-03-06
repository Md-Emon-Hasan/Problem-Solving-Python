# 67. Diagonal Sum of Matrix: Given a square matrix represented as a nested list, write a Python program to calculate the sum of the elements in the main diagonal.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print("Main diagonal sum:", diagonal_sum)