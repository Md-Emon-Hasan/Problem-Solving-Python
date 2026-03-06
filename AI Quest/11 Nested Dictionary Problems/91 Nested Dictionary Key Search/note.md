# Nested Dictionary Key Search

## Problem
Write a Python program to search for a key inside a nested dictionary.

If the key exists → print its value  
Otherwise → print **"Key Not Found"**

Example

Input
```
students = {
 "student1":{"name":"Alice","age":20},
 "student2":{"name":"Bob","age":22}
}

key = name
```

Output
```
Alice
Bob
```

---

# Theory

A **nested dictionary** contains dictionaries inside another dictionary.

To search for a key:

1. Traverse outer dictionary
2. Check inner dictionaries
3. Print value if key exists

Key check pattern:

```
key in dictionary
```

---

# Approach

1. Initialize nested dictionary
2. Take search key as input
3. Traverse outer dictionary
4. Check if key exists in inner dictionary
5. Print value if found

---

# Python Implementation

```python
students = {
 "student1":{"name":"Alice","age":20},
 "student2":{"name":"Bob","age":22}
}

key = "name"

for student in students:
    if key in students[student]:
        print(students[student][key])
```

---

# Key Idea

Nested dictionary search pattern:

```
for key in dict
    if target in dict[key]
```