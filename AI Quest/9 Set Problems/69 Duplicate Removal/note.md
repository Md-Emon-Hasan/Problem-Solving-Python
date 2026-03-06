# Remove Duplicates Using Set

## Problem
Write a Python program that takes a list of elements and creates a **set containing only unique elements**.

Example

Input
```
[1,2,2,3,4,3,5]
```

Output
```
{1,2,3,4,5}
```

---

# Theory

A **set** is a collection of unique elements.

Properties of sets:

- unordered
- no duplicate elements

To remove duplicates from a list, convert the list into a set.

```
set(list)
```

---

# Approach

1. Initialize the list
2. Convert the list into a set
3. Print the result

---

# Python Implementation

```python
numbers = [1,2,2,3,4,3,5]

unique_set = set(numbers)

print(unique_set)
```

---

# Key Idea

Duplicate removal pattern:

```
set(collection)
```