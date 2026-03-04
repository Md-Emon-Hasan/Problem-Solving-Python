# Type Conversion: Convert List of Integers to Strings

## Problem
Given a list of integers, write a Python program to convert each element of the list into a **string**.

Example

Input
```
[1, 2, 3, 4]
```

Output
```
["1", "2", "3", "4"]
```

---

# Theory

Type conversion means converting a value from **one data type to another**.

Python provides built-in functions for type conversion:

```
int()   → convert to integer
float() → convert to float
str()   → convert to string
```

In this problem, we convert **integers → strings** using `str()`.

---

# Approach

1. Take a list of integers
2. Iterate through each element
3. Convert each element using `str()`
4. Store the converted values in a new list

Python's **list comprehension** is the most concise and readable way to do this.

---

# Python Implementation

```python
numbers = [1, 2, 3, 4]

string_list = [str(num) for num in numbers]

print(string_list)
```

Output

```
['1', '2', '3', '4']
```

---

# Key Idea

Use `str()` to convert integers to strings.

Best Pythonic approach:

```
[str(num) for num in numbers]
```