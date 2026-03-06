# 63. Matrix Transpose: Write a Python program to transpose a given matrix represented as a nested list.

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

transpose = []

for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print("Transpose Matrix:")
for r in transpose:
    print(r)