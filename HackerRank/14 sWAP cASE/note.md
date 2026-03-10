# HackerRank – sWAP cASE

## Problem

Convert all uppercase letters to lowercase and lowercase letters to uppercase.

Example

Input

```
HackerRank.com
```

Output

```
hACKERrANK.COM
```

---

# Theory

Python provides a built-in function:

```
swapcase()
```

This converts:

```
Uppercase → Lowercase
Lowercase → Uppercase
```

---

# Approach

1. Read input string
2. Apply `swapcase()`
3. Print result

---

# Python Implementation

```python
def swap_case(s):
    return s.swapcase()

s = input()
print(swap_case(s))
```

---

# Key Idea

String case conversion:

```
swapcase()
```