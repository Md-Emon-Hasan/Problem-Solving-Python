# Sort Nested Lists by Length

## Problem
Given a nested list containing lists of integers, sort the sublists based on their lengths.

Example

Input
```
[[1,2,3],[4],[5,6]]
```

Output
```
[[4],[5,6],[1,2,3]]
```

---

# Theory

Sorting can be performed based on a specific property of elements.

For nested lists, we can sort them based on the **length of each sublist**.

Python provides a `key` parameter for sorting.

Example:

```
sorted(list, key=len)
```

This tells Python to sort using the length of each element.

---

# Approach

1. Initialize the nested list
2. Use the `sorted()` function
3. Set `key=len`
4. Print the sorted result

---

# Python Implementation

```python
nested_list = [[1,2,3],[4],[5,6]]

sorted_list = sorted(nested_list, key=len)

print(sorted_list)
```

---

# Key Idea

Custom sorting pattern:

```
sorted(collection, key=function)
```