# Find Maximum and Minimum in a List

## Problem
Write a Python program to find the **maximum and minimum values** in a given list of integers.

Example

Input
```
[12, 7, 25, 3, 18]
```

Output
```
Maximum = 25
Minimum = 3
```

---

# Theory

To find the maximum and minimum values in a list:

1. Initialize max and min with the **first element** of the list.
2. Traverse the list using a loop.
3. Compare each element with the current max and min.
4. Update values when necessary.

Comparison rules:

```
if element > max → update max
if element < min → update min
```

---

# Approach

1. Initialize list
2. Set

```
max_val = list[0]
min_val = list[0]
```

3. Traverse list
4. Compare and update values

---

# Python Implementation

```python
numbers = [12, 7, 25, 3, 18]

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
        
    if num < min_val:
        min_val = num

print(max_val, min_val)
```

---

# Key Idea

Comparison pattern:

```
if value > max
if value < min
```