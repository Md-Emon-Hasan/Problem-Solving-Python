# Reverse a List (Without Built-in Functions)

## Problem
Write a Python program to **reverse a list** without using built-in functions.

Example

Input
```
[1, 2, 3, 4, 5]
```

Output
```
[5, 4, 3, 2, 1]
```

---

# Theory

A list can be reversed by traversing it **from the last index to the first index**.

If the list length is `n`, the last index is:

```
n - 1
```

By iterating backwards, we can build the reversed list.

---

# Approach

1. Initialize the list
2. Create an empty list
3. Start from the last index
4. Append elements to the new list
5. Move backwards

---

# Python Implementation

```python
numbers = [1, 2, 3, 4, 5]

reversed_list = []

i = len(numbers) - 1

while i >= 0:
    reversed_list.append(numbers[i])
    i -= 1

print(reversed_list)
```

---

# Key Idea

Backward traversal pattern:

```
i = len(list) - 1
while i >= 0
```