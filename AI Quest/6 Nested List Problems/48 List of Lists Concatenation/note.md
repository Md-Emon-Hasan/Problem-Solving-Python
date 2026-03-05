# Concatenate Nested Lists into a Flat List

## Problem
Given a list containing multiple sublists, concatenate all sublists into a **single flat list**.

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

A **nested list** contains lists as elements.

Example:

```
[[1,2],[3,4]]
```

To concatenate them:

1. Traverse each sublist
2. Extract elements from each sublist
3. Add them to a result list

---

# Approach

1. Initialize the nested list
2. Create an empty result list
3. Traverse the nested list
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

Two-level traversal:

```
for sublist in nested_list
    for element in sublist
```