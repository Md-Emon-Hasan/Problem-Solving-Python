# Set Subset Check

## Problem
Given two sets **A** and **B**, check whether **A is a subset of B**.

Example

Input
```
A = {1,2}
B = {1,2,3,4}
```

Output
```
A is a subset of B
```

---

# Theory

A set **A** is a subset of **B** if every element of A exists in B.

Mathematically:

```
A ⊆ B
```

Python provides two ways to check subsets:

1. `issubset()` method
2. `<=` operator

---

# Approach

1. Initialize two sets
2. Check subset condition
3. Print the result

---

# Python Implementation

```python
A = {1,2}
B = {1,2,3,4}

if A.issubset(B):
    print("Subset")
else:
    print("Not a subset")
```

---

# Key Idea

Subset check pattern:

```
A <= B
```