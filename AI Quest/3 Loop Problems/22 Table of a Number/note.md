# Multiplication Table of a Number

## Problem

Write a Python program using a **for loop** to print the multiplication table of a given number **N**.

Example

Input
```
5
```

Output
```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

# Theory

A **multiplication table** shows the result of multiplying a number with a sequence of integers.

Example:

```
5 × 1
5 × 2
5 × 3
...
5 × 10
```

Loops allow repeated execution of operations.

A `for` loop with `range()` is commonly used to generate sequences.

```
range(1, 11)
```

generates numbers from **1 to 10**.

---

# Approach

1. Take integer input `N`
2. Use a `for` loop from **1 to 10**
3. Multiply `N` with the loop variable
4. Print the result

---

# Python Implementation

```python
N = int(input())

for i in range(1, 11):
    print(N, "x", i, "=", N * i)
```

---

# Key Idea

Use iteration with multiplication:

```
N * i
```

inside a loop.