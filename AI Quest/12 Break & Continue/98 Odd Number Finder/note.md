# First Odd Number Finder

## Problem

Write a Python program to find the **first odd number** from a list.

Use:

```
for loop
break
```

---

# Theory

An **odd number** is a number not divisible by 2.

Condition:

```
number % 2 != 0
```

The `break` statement stops the loop immediately when the first odd number is found.

---

# Approach

1. Initialize the list
2. Traverse elements using `for`
3. Check if number is odd
4. Print the number
5. Break the loop

---

# Python Implementation

```python
numbers = [4,8,6,3,10,7]

for num in numbers:
    if num % 2 != 0:
        print(num)
        break
```

---

# Key Idea

Early stop pattern:

```
for item in data:
    if condition:
        break
```