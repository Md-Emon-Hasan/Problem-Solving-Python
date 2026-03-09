# Even Number Printer

## Problem
Write a Python program to print all even numbers from **1 to 20** using a `for` loop and `continue`.

---

# Theory

An **even number** is a number divisible by 2.

Condition:

```
number % 2 == 0
```

The `continue` statement skips the current iteration and moves to the next iteration of the loop.

---

# Approach

1. Loop from `1` to `20`
2. Check if the number is odd
3. If odd → use `continue`
4. Otherwise print the number

---

# Python Implementation

```python
for i in range(1,21):
    if i % 2 != 0:
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