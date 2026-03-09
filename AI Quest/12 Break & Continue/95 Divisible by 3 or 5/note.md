# Divisible by 3 or 5

## Problem
Write a Python program to print numbers from **1 to 50** that are divisible by **3 or 5**.

Use a `for` loop and `continue` to skip numbers that are not divisible by either 3 or 5.

---

# Theory

A number is divisible by 3 if:

```
number % 3 == 0
```

A number is divisible by 5 if:

```
number % 5 == 0
```

The `continue` statement skips the current iteration of the loop.

---

# Approach

1. Loop from `1` to `50`
2. Check if number is not divisible by both 3 and 5
3. If true → use `continue`
4. Otherwise print the number

---

# Python Implementation

```python
for i in range(1,51):
    if i % 3 != 0 and i % 5 != 0:
        continue
    print(i)
```

---

# Key Idea

Skip pattern:

```
if condition:
    continue
```