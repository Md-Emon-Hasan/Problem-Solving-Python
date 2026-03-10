# HackerRank – String Validators

## Problem

Given a string `S`, check whether it contains:

1. Alphanumeric characters
2. Alphabetical characters
3. Digits
4. Lowercase letters
5. Uppercase letters

Print `True` or `False` for each condition.

---

# Theory

Python string validation methods:

```
isalnum() → letter or number
isalpha() → letter
isdigit() → number
islower() → lowercase
isupper() → uppercase
```

---

# Approach

1. Traverse the string
2. Check conditions using string methods
3. Use `any()` to detect at least one match

---

# Python Implementation

```python
s = input()

print(any(c.isalnum() for c in s))
print(any(c.isalpha() for c in s))
print(any(c.isdigit() for c in s))
print(any(c.islower() for c in s))
print(any(c.isupper() for c in s))
```

---

# Key Idea

```
any() + string methods
```