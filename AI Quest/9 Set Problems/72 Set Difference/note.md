# Set Difference

## Problem
Given two sets **A** and **B**, find the difference between them (elements present in A but not in B).

Example

Input
```
A = {1,2,3,4}
B = {3,4,5}
```

Output
```
{1,2}
```

---

# Theory

The **difference** between two sets contains elements that exist in the first set but not in the second set.

Mathematically:

```
A − B
```

Python provides two ways to compute difference:

1. Using `difference()` method
2. Using `-` operator

---

# Approach

1. Initialize two sets
2. Perform difference operation
3. Print the result

---

# Python Implementation

```python
A = {1,2,3,4}
B = {3,4,5}

result = A - B

print(result)
```

---

# Key Idea

Set difference pattern:

```
A - B
```