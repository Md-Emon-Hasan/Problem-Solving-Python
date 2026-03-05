# Matrix Transpose

## Problem
Write a Python program to transpose a matrix represented as a nested list.

Example

Input
```
1 2 3
4 5 6
```

Output
```
1 4
2 5
3 6
```

---

# Theory

Matrix transpose swaps rows and columns.

Rule:

```
transpose[j][i] = matrix[i][j]
```

If matrix size is:

```
m × n
```

Transpose size becomes:

```
n × m
```

---

# Approach

1. Initialize the matrix
2. Create an empty transpose matrix
3. Iterate columns
4. Iterate rows
5. Append elements in swapped order

---

# Python Implementation

```python
matrix = [
    [1,2,3],
    [4,5,6]
]

transpose = []

for j in range(len(matrix[0])):
    row = []
    for i in range(len(matrix)):
        row.append(matrix[i][j])
    transpose.append(row)

print(transpose)
```

---

# Key Idea

Matrix traversal pattern:

```
matrix[i][j] → transpose[j][i]
```