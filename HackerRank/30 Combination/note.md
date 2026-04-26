# HackerRank – itertools.combinations()

## Problem

Given:

```
String S
Integer k
```

Print all **combinations of S up to size k** in **lexicographic order**.

---

# Example

Input

```
HACK 2
```

Output

```
A
C
H
K
AC
AH
AK
CH
CK
HK
```

---

# Key Idea

Use Python's built-in function:

```
itertools.combinations()
```

Syntax

```
combinations(iterable, r)
```

Returns all **r-length combinations** of elements.

---

# Important Step

Sort the string first:

```
sorted(S)
```

Example

```
sorted("HACK")
→ ['A','C','H','K']
```

---

# Implementation

```python
from itertools import combinations

s, k = input().split()
k = int(k)

s = sorted(s)

for i in range(1, k + 1):
    for comb in combinations(s, i):
        print("".join(comb))
```

---

# Complexity

```
Time Complexity ≈ O(nCk)
Space Complexity ≈ O(1)
```

---

# itertools Functions for CP

```
product()
permutations()
combinations()
combinations_with_replacement()
```

These are very common in **competitive programming**.
