# Matrix Multiplication

## Problem
Write a Python program using **nested loops** to multiply two matrices.

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
19 22
43 50
```

---

# Theory

Matrix multiplication rule:

```
C[i][j] = Σ (A[i][k] * B[k][j])
```

Where:

```
i → row index
j → column index
k → summation index
```

Matrix multiplication requires **three nested loops**.

---

# Approach

1. Initialize matrices A and B
2. Create a result matrix with zeros
3. Iterate rows of A
4. Iterate columns of B
5. Multiply and accumulate values

---

# Python Implementation

```python
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

result = [[0, 0],
          [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for row in result:
    print(row)
```

---

# Key Idea

Triple nested loop structure:

```
for i
  for j
    for k
```