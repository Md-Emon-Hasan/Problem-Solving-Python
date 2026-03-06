# Sort a Tuple in Ascending Order

## Problem
Write a Python program to sort a tuple of integers in ascending order.

Example

Input
```
(5, 2, 9, 1, 7)
```

Output
```
(1, 2, 5, 7, 9)
```

---

# Theory

A **tuple** is immutable in Python, meaning its elements cannot be modified.

To sort a tuple:

1. Convert the tuple into a list
2. Sort the list
3. Convert the list back to a tuple

---

# Approach

1. Initialize the tuple
2. Convert tuple to list
3. Sort the list
4. Convert the sorted list back to tuple

---

# Python Implementation

```python
t = (5, 2, 9, 1, 7)

temp_list = list(t)
temp_list.sort()

sorted_tuple = tuple(temp_list)

print(sorted_tuple)
```

---

# Key Idea

Conversion pattern:

```
tuple → list → sort → tuple
```