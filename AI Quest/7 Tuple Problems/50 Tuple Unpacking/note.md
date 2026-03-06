# Tuple Unpacking

## Problem
Given a tuple with three elements `(x, y, z)`, unpack the tuple and assign the values to three variables.

Example

Input
```
(10, 20, 30)
```

Output
```
x = 10
y = 20
z = 30
```

---

# Theory

Tuple unpacking assigns tuple elements to multiple variables.

Syntax:

```
var1, var2, var3 = tuple
```

Python automatically maps:

```
var1 → first element
var2 → second element
var3 → third element
```

---

# Approach

1. Initialize a tuple
2. Unpack it into variables
3. Print the values

---

# Python Implementation

```python
t = (10, 20, 30)

x, y, z = t

print(x, y, z)
```

---

# Key Idea

Tuple unpacking pattern:

```
a, b, c = tuple
```