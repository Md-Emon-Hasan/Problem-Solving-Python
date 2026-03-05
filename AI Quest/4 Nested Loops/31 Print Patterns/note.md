# Right-Angled Triangle Pattern

## Problem
Write a Python program using **nested loops** to print the following pattern:

```
*
**
***
****
*****
```

---

# Theory

Pattern printing problems usually use **nested loops**.

Structure:

```
Outer loop → controls rows
Inner loop → controls symbols per row
```

In this pattern:

```
Row 1 → 1 star
Row 2 → 2 stars
Row 3 → 3 stars
Row 4 → 4 stars
Row 5 → 5 stars
```

The number of stars equals the **row number**.

---

# Approach

1. Set total rows
2. Use outer loop to iterate rows
3. Use inner loop to print stars
4. Print new line after each row

---

# Python Implementation

```python
rows = 5

for i in range(1, rows+1):
    for j in range(i):
        print("*", end="")
    print()
```

---

# Key Idea

Nested loop pattern:

```
for row in range():
    for column in range(row):
```