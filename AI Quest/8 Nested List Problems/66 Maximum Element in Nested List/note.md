# Maximum Element in a Nested List

## Problem
Write a Python program to find the **maximum element** in a nested list of integers.

Example

Input
```
[[1,2,3],[4,9,6],[7,8]]
```

Output
```
9
```

---

# Theory

A nested list contains lists inside a list.

To find the maximum value:

1. Traverse all elements
2. Compare each element with the current maximum
3. Update the maximum if a larger value is found

---

# Approach

1. Initialize the nested list
2. Set the first element as the initial maximum
3. Traverse each sublist
4. Traverse elements inside each sublist
5. Update the maximum value when needed

---

# Python Implementation

```python
nested_list = [[1,2,3],[4,9,6],[7,8]]

max_value = nested_list[0][0]

for sublist in nested_list:
    for num in sublist:
        if num > max_value:
            max_value = num

print(max_value)
```

---

# Key Idea

Comparison pattern:

```
if value > max_value
    max_value = value
```