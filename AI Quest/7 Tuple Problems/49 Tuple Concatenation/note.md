# Tuple Concatenation

## Problem
Write a Python program to concatenate two tuples and create a new tuple.

Example

Input
```
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
```

Output
```
(1, 2, 3, 4, 5, 6)
```

---

# Theory

A **tuple** is an ordered and immutable collection in Python.

Tuple concatenation combines two tuples into a new tuple.

Operator used:

```
+
```

Example:

```
tuple1 + tuple2
```

---

# Approach

1. Initialize two tuples
2. Use the `+` operator
3. Store the result in a new tuple

---

# Python Implementation

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print(result)
```

---

# Key Idea

Tuple concatenation pattern:

```
tuple1 + tuple2
```