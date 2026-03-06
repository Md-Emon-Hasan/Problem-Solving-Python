# Dictionary Merging

## Problem
Given two dictionaries, merge them into a single dictionary.

Example

Input
```
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}
```

Output
```
{"a":1,"b":2,"c":3,"d":4}
```

---

# Theory

Dictionary merging combines key-value pairs from multiple dictionaries into one.

If duplicate keys exist:

```
second dictionary value overwrites the first
```

Common Python methods:

```
dict1.update(dict2)
{**dict1, **dict2}
dict1 | dict2
```

---

# Approach

1. Initialize two dictionaries
2. Perform merge operation
3. Print the merged dictionary

---

# Python Implementation

```python
dict1 = {"a":1,"b":2}
dict2 = {"c":3,"d":4}

merged_dict = {**dict1, **dict2}

print(merged_dict)
```

---

# Key Idea

Dictionary merge pattern:

```
{**dict1, **dict2}
```