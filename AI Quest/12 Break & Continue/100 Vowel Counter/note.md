# Vowel Counter

## Problem

Write a Python program that counts the number of **vowels** in a string.

Use:

```
for loop
continue
```

to skip non-vowel characters.

---

# Theory

Vowels are:

```
a, e, i, o, u
```

Both uppercase and lowercase vowels should be considered.

To check membership:

```
char in vowels
```

---

# Approach

1. Take string input
2. Define vowel characters
3. Initialize counter
4. Traverse string
5. Skip non-vowels using `continue`
6. Count vowels

---

# Python Implementation

```python
text = input()

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char not in vowels:
        continue
    count += 1

print(count)
```

---

# Key Idea

Filtering pattern:

```
for element in data
    if invalid:
        continue
    process valid
```