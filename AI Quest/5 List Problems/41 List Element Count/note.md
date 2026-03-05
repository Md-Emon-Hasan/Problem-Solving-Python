# Count Occurrences of an Element in a List

## Problem
Write a Python program to count how many times a **specific element** appears in a list.

Example

Input
```
list = [1, 2, 3, 2, 4, 2]
element = 2
```

Output
```
3
```

---

# Theory

To count occurrences of an element:

1. Traverse the list
2. Compare each element with the target value
3. Increment the counter if they match

Comparison condition:

```
element == target
```

---

# Approach

1. Initialize the list
2. Set the target element
3. Initialize `count = 0`
4. Traverse the list
5. If the element matches the target, increase the count

---

# Python Implementation

```python
numbers = [1, 2, 3, 2, 4, 2]

target = 2
count = 0

for num in numbers:
    if num == target:
        count += 1

print(count)
```

---

# Key Idea

Counting pattern:

```
if element == target:
    count += 1
```