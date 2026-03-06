# Tuple Packing

## Problem
Write a Python program to pack three variables into a single tuple and print the tuple.

Example

Input
```
x = 10
y = 20
z = 30
```

Output
```
(10, 20, 30)
```

---

# Theory

Tuple packing combines multiple values into a single tuple.

Syntax:

```
tuple = (value1, value2, value3)
```

Python also allows packing without parentheses:

```
tuple = value1, value2, value3
```

---

# Approach

1. Initialize variables
2. Pack them into a tuple
3. Print the tuple

---

# Python Implementation

```python
x = 10
y = 20
z = 30

t = (x, y, z)

print(t)
```

---

# Key Idea

Packing pattern:

```
tuple = value1, value2, value3
```