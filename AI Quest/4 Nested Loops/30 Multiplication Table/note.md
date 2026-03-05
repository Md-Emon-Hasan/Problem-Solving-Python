# Multiplication Tables (1 to 10)

## Problem
Write a Python program using **nested loops** to print multiplication tables from **1 to 10**.

Example Output

```
1 x 1 = 1
1 x 2 = 2
...
1 x 10 = 10

2 x 1 = 2
2 x 2 = 4
...
2 x 10 = 20
```

---

# Theory

This problem uses **nested loops**.

A nested loop means a loop inside another loop.

Structure:

```
for outer_loop:
    for inner_loop:
```

In multiplication tables:

- Outer loop → selects the table number
- Inner loop → multiplies numbers from **1 to 10**

---

# Approach

1. Use outer loop from **1 to 10**
2. Use inner loop from **1 to 10**
3. Multiply outer loop value with inner loop value
4. Print formatted result

---

# Python Implementation

```python
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()
```

---

# Key Idea

Nested loop pattern:

```
for i in range():
    for j in range():
```