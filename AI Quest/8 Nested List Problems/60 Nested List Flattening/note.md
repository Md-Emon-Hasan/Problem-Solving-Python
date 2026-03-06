# Flatten a Nested List

## Problem
Write a Python program to flatten a nested list and convert it into a single-dimensional list.

Example

Input
```
[[1,2],[3,4],[5,6]]
```

Output
```
[1,2,3,4,5,6]
```

---

# Theory

A nested list contains lists as elements.

Example:

```
[[1,2],[3,4]]
```

Flattening means extracting all elements from sublists and combining them into a single list.

This requires **two levels of iteration**.

---

# Approach

1. Initialize the nested list
2. Create an empty result list
3. Traverse each sublist
4. Extract elements from sublists
5. Append them to the result list

---

# Python Implementation

```python
nested_list = [[1,2],[3,4],[5,6]]

flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print(flat_list)
```

---

# Key Idea

Nested traversal pattern:

```
for sublist in nested_list
    for element in sublist
```