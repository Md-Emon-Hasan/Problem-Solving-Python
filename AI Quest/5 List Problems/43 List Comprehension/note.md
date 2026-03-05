# Squares of List Elements Using List Comprehension

## Problem
Given a list of integers, create a new list containing the **square of each element** using **list comprehension**.

Example

Input
```
[1, 2, 3, 4, 5]
```

Output
```
[1, 4, 9, 16, 25]
```

---

# Theory

List comprehension is a concise way to create lists in Python.

General syntax:

```
[expression for element in iterable]
```

It replaces loops used to build lists.

Example:

```
[num*num for num in numbers]
```

---

# Approach

1. Initialize the list
2. Use list comprehension
3. Apply the square operation

---

# Python Implementation

```python
numbers = [1, 2, 3, 4, 5]

squares = [num*num for num in numbers]

print(squares)
```

---

# Key Idea

List comprehension pattern:

```
[expression for element in iterable]
```