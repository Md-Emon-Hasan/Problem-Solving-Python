# Matrix Addition

## Problem
Write a Python program to **add two matrices** represented as nested lists.

Example

Matrix A
```
1 2
3 4
```

Matrix B
```
5 6
7 8
```

Result
```
6 8
10 12
```

---

# Theory

Matrix addition is performed by adding **corresponding elements** of two matrices.

Rule:

```
C[i][j] = A[i][j] + B[i][j]
```

Both matrices must have the **same dimensions**.

Matrices are represented in Python as **nested lists**.

Example:

```
[[1,2],
 [3,4]]
```

---

# Approach

1. Initialize matrices
2. Create an empty result matrix
3. Iterate rows
4. Iterate columns
5. Add corresponding elements

---

# Python Implementation

```python
A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print(result)
```

---

# Key Idea

Matrix traversal pattern:

```
for i in rows
    for j in columns
```