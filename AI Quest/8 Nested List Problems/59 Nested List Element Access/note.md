# Access Elements in a Nested List

## Problem
Given a nested list, access and print specific elements from it.

Example

Input
```
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
```

Output
```
6
2
```

---

# Theory

A nested list contains lists inside a list.

Example:

```
[[1,2,3],[4,5,6]]
```

To access elements, use **two indexes**:

```
list[row][column]
```

---

# Approach

1. Initialize the nested list
2. Select row index
3. Select column index
4. Print the element

---

# Python Implementation

```python
nested_list = [[1,2,3],[4,5,6],[7,8,9]]

print(nested_list[1][2])
print(nested_list[0][1])
```

---

# Key Idea

2D indexing pattern:

```
matrix[row][column]
```