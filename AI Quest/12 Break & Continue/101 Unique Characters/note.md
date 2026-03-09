# Unique Characters Checker

## Problem

Write a Python program that checks whether a string contains **all unique characters**.

Use:

```
for loop
break
```

when a repeated character is found.

---

# Theory

A string has **unique characters** if no character appears more than once.

Example:

```
abc → unique
hello → not unique
```

To track visited characters we use a **set**.

A set stores unique elements and provides fast lookup.

---

# Approach

1. Take string input
2. Create empty set
3. Traverse string
4. Check if character already exists
5. If exists → break
6. Otherwise add character to set

---

# Python Implementation

```python
text = input()

seen = set()

for char in text:
    if char in seen:
        print("Duplicate found")
        break
    seen.add(char)
else:
    print("All characters unique")
```

---

# Key Idea

Duplicate detection pattern:

```
seen = set()

for item in data:
    if item in seen:
        break
    seen.add(item)
```