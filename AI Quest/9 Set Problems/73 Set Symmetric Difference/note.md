# Set Symmetric Difference

## Problem
Given two sets **A** and **B**, find the **symmetric difference** between them.

Example

Input
```
A = {1,2,3,4}
B = {3,4,5,6}
```

Output
```
{1,2,5,6}
```

---

# Theory

The **symmetric difference** contains elements that exist in either set but not in both.

Mathematically:

```
(A - B) ∪ (B - A)
```

Python provides two ways to compute symmetric difference:

1. Using `symmetric_difference()` method
2. Using `^` operator

---

# Approach

1. Initialize two sets
2. Perform symmetric difference
3. Print the result

---

# Python Implementation

```python
A = {1,2,3,4}
B = {3,4,5,6}

result = A ^ B

print(result)
```

---

# Key Idea

Symmetric difference pattern:

```
A ^ B
```