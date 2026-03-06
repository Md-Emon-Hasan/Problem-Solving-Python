# Dictionary Key Check

## Problem
Write a Python program to check whether a given key exists in a dictionary.

If the key exists → print **"Key Found"**  
Otherwise → print **"Key Not Found"**

Example

Input
```
dictionary = {"apple":10,"banana":5,"orange":8}
key = banana
```

Output
```
Key Found
```

---

# Theory

Dictionaries store data in **key-value pairs**.

To check whether a key exists in a dictionary, Python provides the **`in` operator**.

Syntax:

```
key in dictionary
```

Returns:

```
True / False
```

---

# Approach

1. Initialize the dictionary
2. Take the key as input
3. Use `in` operator to check existence
4. Print the result

---

# Python Implementation

```python
items = {"apple":10,"banana":5,"orange":8}

key = input()

if key in items:
    print("Key Found")
else:
    print("Key Not Found")
```

---

# Key Idea

Dictionary membership pattern:

```
key in dictionary
```