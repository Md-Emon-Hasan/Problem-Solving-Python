# Dictionary Frequency Count

## Problem
Write a Python program that takes a string and creates a dictionary where:

```
key → character
value → frequency of that character
```

Example

Input
```
hello
```

Output
```
{'h':1,'e':1,'l':2,'o':1}
```

---

# Theory

A **frequency dictionary** counts how many times each element appears.

Steps:

1. Traverse the string
2. Check if the character exists in dictionary
3. Increase count if exists
4. Otherwise initialize count as 1

---

# Approach

1. Take input string
2. Initialize empty dictionary
3. Traverse characters
4. Update frequency
5. Print dictionary

---

# Python Implementation

```python
text = "hello"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)
```

---

# Key Idea

Frequency counting pattern:

```
if key in dict
    dict[key] += 1
else
    dict[key] = 1
```