# Main Diagonal Sum of a Matrix

## Problem
Given a square matrix represented as a nested list, calculate the **sum of the elements in the main diagonal**.

Example

Input
```
1 2 3
4 5 6
7 8 9
```

Output
```
15
```

---

# Theory

A **square matrix** has equal rows and columns.

The **main diagonal** contains elements where:

```
row index = column index
```

Example:

```
matrix[i][i]
```

Main diagonal elements:

```
1, 5, 9
```

---

# Approach

1. Initialize the matrix
2. Initialize a sum variable
3. Traverse indices
4. Add elements where `i == j`

---

# Python Implementation

```python
matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

diagonal_sum = 0

for i in range(len(matrix)):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)
```

---

# Key Idea

Diagonal access pattern:

```
matrix[i][i]
```