# Set Union

## Problem
Given two sets **A** and **B**, find their **union** and print all distinct elements from both sets.

Example

Input
```
A = {1,2,3}
B = {3,4,5}
```

Output
```
{1,2,3,4,5}
```

---

# Theory

The **union** of two sets contains all elements from both sets.

Mathematically:

```
A ∪ B
```

Since sets store only unique elements, duplicates are automatically removed.

Python provides two ways to compute union:

1. Using the `union()` method
2. Using the `|` operator

---

# Approach

1. Initialize two sets
2. Compute union
3. Print the result

---

# Python Implementation

```python
A = {1,2,3}
B = {3,4,5}

result = A.union(B)

print(result)
```

---

# Key Idea

Union operation pattern:

```
A | B
```