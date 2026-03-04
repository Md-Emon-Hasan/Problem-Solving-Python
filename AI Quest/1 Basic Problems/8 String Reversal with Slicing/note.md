# String Reversal Using Slicing

## Problem
Write a Python function to reverse a given string **using slicing**.

Example

Input
```
hello
```

Output
```
olleh
```

---

# Theory

A **string** is a sequence of characters.

Python provides a powerful feature called **slicing** which allows extracting or manipulating parts of a string.

General syntax:

```
string[start : stop : step]
```

If the step is **-1**, Python traverses the string **from end to beginning**, effectively reversing it.

```
[::-1]
```

This is the most common and Pythonic method to reverse a string.

---

# Approach

1. Take a string as input
2. Use slicing with step `-1`
3. Return the reversed string

---

# Python Implementation

```python
def reverse_string(s):
    return s[::-1]
```

Example

```python
print(reverse_string("hello"))
```

Output

```
olleh
```

---

# Key Idea

Use slicing with a negative step:

```
string[::-1]
```

This reverses the string efficiently.