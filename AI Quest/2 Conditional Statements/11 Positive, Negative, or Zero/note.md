# Positive, Negative, or Zero

## Problem
Write a Python program that takes a number as input and prints whether it is **positive**, **negative**, or **zero**.

Example

Input
```
-5
```

Output
```
Negative
```

---

# Theory

Numbers can be categorized into three types based on their value relative to zero.

```
number > 0  → Positive
number < 0  → Negative
number = 0  → Zero
```

To implement this logic, Python uses **conditional statements**.

```
if
elif
else
```

These allow the program to execute different blocks of code based on conditions.

---

# Approach

1. Take a number as input
2. Check if the number is greater than zero
3. Check if the number is less than zero
4. Otherwise the number is zero

---

# Python Implementation

```python
num = float(input())

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
```

---

# Key Idea

Use conditional statements:

```
if num > 0
elif num < 0
else
```

to classify the number.