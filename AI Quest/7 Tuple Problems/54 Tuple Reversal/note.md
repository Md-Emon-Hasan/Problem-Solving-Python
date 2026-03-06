# Reverse a Tuple (Without Built-in Functions)

## Problem
Write a Python program to reverse a tuple without using built-in functions.

Example

Input
```
(1, 2, 3, 4)
```

Output
```
(4, 3, 2, 1)
```

---

# Theory

Since tuples are immutable, we cannot modify them directly.

Instead, we create a new tuple and append elements in reverse order.

To traverse backwards:

```
index = len(tuple) - 1
```

---

# Approach

1. Initialize the tuple
2. Create an empty tuple
3. Start from the last index
4. Append elements in reverse order

---

# Python Implementation

```python
t = (1, 2, 3, 4)

reversed_tuple = ()

i = len(t) - 1

while i >= 0:
    reversed_tuple += (t[i],)
    i -= 1

print(reversed_tuple)
```

---

# Key Idea

Backward traversal pattern:

```
i = len(sequence) - 1
```