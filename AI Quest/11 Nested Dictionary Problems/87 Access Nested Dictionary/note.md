# Access Nested Dictionary

## Problem
Given a nested dictionary containing student details, access and print:

- name
- age
- address

Example

Input
```
students = {
 "student1":{
  "name":"Alice",
  "age":20,
  "address":"New York"
 }
}
```

Output
```
Name: Alice
Age: 20
Address: New York
```

---

# Theory

A **nested dictionary** is a dictionary inside another dictionary.

Structure:

```
outer_dictionary[key][inner_key]
```

Example:

```
students["student1"]["name"]
```

This accesses the inner value.

---

# Approach

1. Initialize nested dictionary
2. Access outer key
3. Access inner keys
4. Print the values

---

# Python Implementation

```python
students = {
 "student1":{
  "name":"Alice",
  "age":20,
  "address":"New York"
 }
}

print(students["student1"]["name"])
print(students["student1"]["age"])
print(students["student1"]["address"])
```

---

# Key Idea

Nested dictionary access pattern:

```
dict[key1][key2]
```