# Convert Tuple to List

## Problem
Write a Python program to convert a tuple into a list.

Example

Input
```
(1, 2, 3, 4)
```

Output
```
[1, 2, 3, 4]
```

---

# Theory

A tuple is an immutable sequence in Python.

To convert a tuple into a list, we use:

```
list(tuple)
```

This creates a new list containing the same elements.

---

# Python Implementation

```python
t = (1, 2, 3, 4)

converted_list = list(t)

print(converted_list)
```

---

# Key Idea

Data structure conversion:

```
tuple → list
```