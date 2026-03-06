# 68. Nested List Element Search: Write a Python program to search for a specific element in a nested list and return its position (row and column indices).

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

target = int(input("Enter element to search: "))

found = False

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == target:
            print("Element found at position:", (i, j))
            found = True
            break

    if found:
        break

if not found:
    print("Element not found")