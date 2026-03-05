# Sorting a List (Ascending Order)

## Problem
Write a Python program to sort a list of integers in **ascending order**.

Example

Input
```
[5, 2, 9, 1, 7]
```

Output
```
[1, 2, 5, 7, 9]
```

---

# Theory

Sorting arranges elements in a specific order.

Ascending order means:

```
small → large
```

A simple sorting algorithm is **Bubble Sort**.

It repeatedly compares adjacent elements and swaps them if they are in the wrong order.

---

# Approach

1. Iterate through the list
2. Compare adjacent elements
3. Swap if the order is incorrect
4. Repeat until the list is sorted

---

# Python Implementation

```python
numbers = [5, 2, 9, 1, 7]

n = len(numbers)

for i in range(n):
    for j in range(0, n-i-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

print(numbers)
```

---

# Key Idea

Adjacent comparison and swap:

```
if a > b:
    swap
```