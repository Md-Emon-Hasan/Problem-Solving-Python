# Set Superset Check

## Problem
Given two sets **A** and **B**, check whether **A is a superset of B**.

Example

Input
```
A = {1,2,3,4}
B = {2,3}
```

Output
```
A is a superset of B
```

---

# Theory

A set **A** is a superset of **B** if all elements of **B** exist in **A**.

Mathematically:

```
A ⊇ B
```

Python provides two ways to check this:

1. `issuperset()` method
2. `>=` operator

---

# Approach

1. Initialize two sets
2. Check the superset condition
3. Print the result

---

# Python Implementation

```python
A = {1,2,3,4}
B = {2,3}

if A.issuperset(B):
    print("Superset")
else:
    print("Not a superset")
```

---

# Key Idea

Superset pattern:

```
A >= B
```