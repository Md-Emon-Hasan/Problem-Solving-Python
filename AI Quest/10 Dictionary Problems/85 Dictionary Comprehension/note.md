# Dictionary Comprehension

## Problem
Given a list of integers, create a dictionary where:

```
key   → list element
value → square of the element
```

Example

Input
```
[1,2,3,4]
```

Output
```
{1:1, 2:4, 3:9, 4:16}
```

---

# Theory

Dictionary comprehension provides a concise way to create dictionaries.

Syntax:

```
{key:value for element in iterable}
```

Example:

```
{x:x**2 for x in numbers}
```

Where:

```
x → element
x**2 → square
```

---

# Approach

1. Initialize the list
2. Use dictionary comprehension
3. Print the resulting dictionary

---

# Python Implementation

```python
numbers = [1,2,3,4]

square_dict = {x:x**2 for x in numbers}

print(square_dict)
```

---

# Key Idea

Dictionary comprehension pattern:

```
{key:value for item in iterable}
```