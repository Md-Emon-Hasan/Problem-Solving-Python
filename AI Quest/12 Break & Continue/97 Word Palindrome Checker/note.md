# Word Palindrome Checker

## Problem

Write a Python program to check whether a word is a palindrome.

Conditions:

- If word length < 3 → skip using `continue`
- Otherwise check palindrome

---

# Theory

A **palindrome** is a word that reads the same forwards and backwards.

Example:

```
madam
level
racecar
```

Python can reverse a string using slicing:

```
word[::-1]
```

---

# Approach

1. Take word input
2. Check length
3. If length < 3 → continue
4. Reverse string
5. Compare original and reversed string

---

# Python Implementation

```python
while True:
    word = input()

    if len(word) < 3:
        continue

    if word == word[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

    break
```

---

# Key Idea

Palindrome check pattern:

```
string == string[::-1]
```