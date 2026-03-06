# Dictionary Value Search

## Problem
Given a dictionary of items and their prices, search for an item based on its price and print the item name.

Example

Input
```
items = {"apple":100, "banana":60, "orange":80}
price = 80
```

Output
```
orange
```

---

# Theory

A dictionary stores data in **key-value pairs**.

Normally we search:

```
key → value
```

But in this problem we need to search:

```
value → key
```

To do this we must iterate through the dictionary.

Python provides:

```
dictionary.items()
```

Which returns:

```
(key, value)
```

pairs.

---

# Approach

1. Initialize the dictionary
2. Take the target price
3. Traverse the dictionary using `items()`
4. Compare the value
5. Print the key when match found

---

# Python Implementation

```python
items = {"apple":100, "banana":60, "orange":80}

price = 80

for item, value in items.items():
    if value == price:
        print(item)
```

---

# Key Idea

Dictionary traversal pattern:

```
for key, value in dictionary.items()
```