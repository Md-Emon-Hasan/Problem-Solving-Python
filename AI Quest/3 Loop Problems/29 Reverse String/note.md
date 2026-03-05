# Reverse String Using While Loop

## Problem
Write a Python program using a **while loop** to reverse a given string.

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

To reverse a string, we read characters **from the last index to the first index**.

If the string length is `n`, the last index is:

```
n - 1
```

We can iterate backward using a loop.

---

# Approach

1. Take string input
2. Set index = `len(string) - 1`
3. Initialize empty string
4. Use `while` loop while index ≥ 0
5. Append characters in reverse order
6. Decrease index

---

# Python Implementation

```python
text = input()

reversed_str = ""
i = len(text) - 1

while i >= 0:
    reversed_str += text[i]
    i -= 1

print(reversed_str)
```

---

# Key Idea

Traverse the string **from end to start**:

```
i = len(string) - 1
while i >= 0
```