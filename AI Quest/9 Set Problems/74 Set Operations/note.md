# Multiple Set Operations

## Problem
Given three sets **A**, **B**, and **C**, perform the following operations:

1. Intersection of A and B
2. Union of B and C
3. Difference of C and A

Example

Input
```
A = {1,2,3}
B = {2,3,4}
C = {3,4,5}
```

Output
```
Intersection (A,B) → {2,3}
Union (B,C) → {2,3,4,5}
Difference (C,A) → {4,5}
```

---

# Theory

Set operations allow us to combine and compare sets.

Common operations:

```
Intersection → A & B
Union → A | B
Difference → A - B
```

These operations follow standard mathematical set rules.

---

# Approach

1. Initialize three sets
2. Compute intersection
3. Compute union
4. Compute difference
5. Print the results

---

# Python Implementation

```python
A = {1,2,3}
B = {2,3,4}
C = {3,4,5}

print(A & B)
print(B | C)
print(C - A)
```

---

# Key Idea

Set operation patterns:

```
A & B
A | B
A - B
```