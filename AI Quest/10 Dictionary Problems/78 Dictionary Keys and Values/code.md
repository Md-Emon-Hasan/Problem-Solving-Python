# Dictionary Keys and Values

## Problem
Write a Python program that prints all the **keys** and **values** of a dictionary in separate lines.

Example

Input
```
students = {"Alice":85, "Bob":90, "Charlie":88}
```

Output
```
Keys:
Alice
Bob
Charlie

Values:
85
90
88
```

---

# Theory

A dictionary stores data in **key-value pairs**.

To access dictionary elements:

```
dictionary.keys()
dictionary.values()
```

- `keys()` → returns all keys
- `values()` → returns all values

---

# Approach

1. Initialize the dictionary
2. Use `keys()` to iterate through keys
3. Use `values()` to iterate through values
4. Print them separately

---

# Python Implementation

```python
students = {"Alice":85, "Bob":90, "Charlie":88}

for key in students.keys():
    print(key)

for value in students.values():
    print(value)
```

---

# Key Idea

Dictionary traversal pattern:

```
for key in dictionary
for value in dictionary.values()
```