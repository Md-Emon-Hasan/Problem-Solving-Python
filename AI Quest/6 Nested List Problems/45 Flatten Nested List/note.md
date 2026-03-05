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

Flattening means converting this structure into a single list.

This requires iterating through:

1. Each sublist
2. Each element inside the sublist

---

# Approach

1. Initialize the nested list
2. Create an empty list
3. Traverse the nested list
4. Extract elements from each sublist
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

Two-level iteration:

```
for sublist in nested_list
    for element in sublist
```