# Set Intersection

## Problem
Given two sets **A** and **B**, find their intersection and print the common elements.

Example

Input
```
A = {1,2,3,4}
B = {3,4,5,6}
```

Output
```
{3,4}
```

---

# Theory

The **intersection** of two sets contains elements that exist in **both sets**.

Mathematically:

```
A ∩ B
```

Python provides two ways to compute intersection:

1. Using the `intersection()` method
2. Using the `&` operator

---

# Approach

1. Initialize two sets
2. Compute intersection
3. Print the result

---

# Python Implementation

```python
A = {1,2,3,4}
B = {3,4,5,6}

common = A.intersection(B)

print(common)
```

---

# Key Idea

Set intersection pattern:

```
A & B
```