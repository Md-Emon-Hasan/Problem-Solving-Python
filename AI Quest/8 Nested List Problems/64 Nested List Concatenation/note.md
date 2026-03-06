# Concatenate Nested Lists into a Flat List

## Problem
Given a list containing nested lists, concatenate all sublists into a single flat list.

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

A nested list contains lists inside a list.

Example:

```
[[1,2],[3,4]]
```

To concatenate them into a flat list:

1. Traverse each sublist
2. Extract each element
3. Append them to a result list

---

# Approach

1. Initialize the nested list
2. Create an empty result list
3. Traverse each sublist
4. Traverse elements inside each sublist
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