# Dictionary Sorting by Value

## Problem
Given a dictionary with names as keys and ages as values, sort the dictionary based on age in ascending order.

Example

Input
```
{"Alice":25,"Bob":20,"Charlie":30}
```

Output
```
{"Bob":20,"Alice":25,"Charlie":30}
```

---

# Theory

Dictionaries can be sorted using the `sorted()` function.

```
sorted(dictionary.items(), key=function)
```

`items()` returns key-value pairs.

To sort by **value**:

```
key=lambda x: x[1]
```

Where:

```
x[0] → key
x[1] → value
```

---

# Approach

1. Initialize the dictionary
2. Convert dictionary to key-value pairs
3. Sort using `sorted()`
4. Convert result back to dictionary

---

# Python Implementation

```python
people = {"Alice":25,"Bob":20,"Charlie":30}

sorted_people = dict(sorted(people.items(), key=lambda x: x[1]))

print(sorted_people)
```

---

# Key Idea

Dictionary sorting pattern:

```
sorted(dict.items(), key=lambda x: x[1])
```