# Dictionary Key Removal

## Problem
Given a dictionary of items and their quantities, remove a specific item based on user input.

Example

Input
```
items = {"apple":10,"banana":5,"orange":8}
remove = "banana"
```

Output
```
{"apple":10,"orange":8}
```

---

# Theory

Dictionaries store data as **key-value pairs**.

To remove a key from a dictionary, Python provides:

```
pop(key)
del dictionary[key]
```

Using `pop(key, None)` avoids errors if the key does not exist.

---

# Approach

1. Initialize the dictionary
2. Take the key to remove
3. Use `pop()` to remove it
4. Print the updated dictionary

---

# Python Implementation

```python
items = {"apple":10,"banana":5,"orange":8}

key = input()

items.pop(key, None)

print(items)
```

---

# Key Idea

Dictionary removal pattern:

```
dictionary.pop(key)
```