# Chessboard Pattern (8×8)

## Problem
Write a Python program using nested loops to print a chessboard pattern using **X** and **O**.

Example

```
X O X O X O X O
O X O X O X O X
X O X O X O X O
...
```

---

# Theory

A chessboard pattern alternates between two characters.

The pattern depends on the **sum of row and column indices**.

Rule:

```
(i + j) % 2 == 0 → X
(i + j) % 2 == 1 → O
```

---

# Python Implementation

```python
size = 8

for i in range(size):
    for j in range(size):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
```

---

# Key Idea

Alternating pattern using:

```
(i + j) % 2
```