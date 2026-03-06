# Dictionary Manipulation

## Problem
Given a dictionary with student names as keys and scores as values:

1. Add a new student to the dictionary
2. Update the score of an existing student

Example

Input
```
students = {"Alice":85, "Bob":90}
```

Output
```
{"Alice":92, "Bob":90, "Charlie":88}
```

---

# Theory

A dictionary stores data in **key-value pairs**.

Structure:

```
key : value
```

To add or update values:

```
dictionary[key] = value
```

If the key already exists → value is updated  
If the key does not exist → a new key-value pair is added

---

# Approach

1. Initialize the dictionary
2. Add a new key-value pair
3. Update an existing value
4. Print the dictionary

---

# Python Implementation

```python
students = {"Alice":85, "Bob":90}

students["Charlie"] = 88
students["Alice"] = 92

print(students)
```

---

# Key Idea

Dictionary update pattern:

```
dictionary[key] = value
```