# Sum of First N Natural Numbers

## Problem

Write a Python program using a **for loop** to calculate the sum of the first **N natural numbers**, where **N is taken as input** from the user.

Example

Input
```
5
```

Output
```
15
```

---

# Theory

Natural numbers start from:

```
1, 2, 3, 4, ...
```

To compute the sum of the first **N natural numbers**, we add all numbers from **1 to N**.

Example:

```
1 + 2 + 3 + 4 + 5 = 15
```

Python uses **loops** to repeatedly perform operations.

A `for` loop with `range()` can iterate through numbers sequentially.

```
range(1, N+1)
```

This generates numbers from **1 to N**.

---

# Approach

1. Take integer input `N`
2. Initialize `total = 0`
3. Use a `for` loop from `1` to `N`
4. Add each number to `total`
5. Print the final sum

---

# Python Implementation

```python
N = int(input())

total = 0

for i in range(1, N+1):
    total += i

print(total)
```

---

# Key Idea

Use an **accumulator pattern** inside a loop:

```
total += i
```