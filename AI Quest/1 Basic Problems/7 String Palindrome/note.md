# String Palindrome

## Problem
Write a Python function to check if a given string is a **palindrome** or not.

Example

Input
```
madam
```

Output
```
Palindrome
```

---

# Theory

A **palindrome** is a string that reads the same **forward and backward**.

Examples

```
madam
level
racecar
```

Non-palindrome example

```
hello
```

The idea is simple:

If

```
original_string == reversed_string
```

then the string is a **palindrome**.

Python provides a simple way to reverse strings using **slicing**.

```
string[::-1]
```

This reads the string from **end to beginning**.

---

# Approach

1. Take a string as input
2. Reverse the string
3. Compare the original string with the reversed string
4. If both are equal → Palindrome

---

# Python Implementation

```python
def is_palindrome(s):
    return s == s[::-1]
```

Example

```python
print(is_palindrome("madam"))
```

Output

```
True
```

---

# Key Idea

Reverse the string and compare:

```
s == s[::-1]
```