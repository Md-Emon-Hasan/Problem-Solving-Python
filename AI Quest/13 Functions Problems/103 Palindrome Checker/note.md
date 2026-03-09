# Palindrome Checker Function

## Problem

Write a Python function called `is_palindrome` that checks whether a string is a palindrome.

Return:

```
True  → if palindrome
False → otherwise
```

---

# Theory

A **palindrome** is a string that reads the same forward and backward.

Example:

```
madam
level
racecar
```

Python allows reversing strings using slicing:

```
string[::-1]
```

---

# Approach

1. Define function
2. Reverse string
3. Compare with original
4. Return boolean result

---

# Python Implementation

```python
def is_palindrome(word):

    if word == word[::-1]:
        return True
    else:
        return False


print(is_palindrome("madam"))
print(is_palindrome("hello"))
```

---

# Key Idea

Palindrome check pattern:

```
string == string[::-1]
```