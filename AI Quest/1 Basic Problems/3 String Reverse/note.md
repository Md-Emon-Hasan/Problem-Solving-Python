# Reverse a String

## Problem
Write a Python function to reverse a given string and return the reversed string.

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

Reversing a string means **reading the characters in the opposite order**.

Example

```
hello → olleh
```

Python provides a powerful feature called **slicing** that allows extracting parts of a string.

Syntax

```
string[start:stop:step]
```

If the step is **-1**, Python traverses the string **from end to beginning**, effectively reversing it.

```
[::-1]
```

This is the most common and Pythonic way to reverse a string.

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

String slicing with step `-1` reverses a string.

```
string[::-1]
```