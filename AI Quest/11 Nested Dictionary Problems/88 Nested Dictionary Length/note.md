# Nested Dictionary Length

## Problem
Write a Python program to calculate the **total number of key-value pairs** in a nested dictionary.

Example

Input
```
students = {
 "student1":{"name":"Alice","age":20},
 "student2":{"name":"Bob","age":22}
}
```

Output
```
4
```

---

# Theory

A nested dictionary is a dictionary containing other dictionaries.

To count all key-value pairs:

1. Traverse the outer dictionary
2. Calculate the length of each inner dictionary
3. Add them together

Use:

```
len(inner_dictionary)
```

---

# Approach

1. Initialize nested dictionary
2. Create a counter variable
3. Traverse outer dictionary
4. Add lengths of inner dictionaries
5. Print the total count

---

# Python Implementation

```python
students = {
 "student1":{"name":"Alice","age":20},
 "student2":{"name":"Bob","age":22}
}

total = 0

for key in students:
    total += len(students[key])

print(total)
```

---

# Key Idea

Nested dictionary counting pattern:

```
for key in dict
    total += len(dict[key])
```