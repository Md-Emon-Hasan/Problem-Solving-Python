# Sum of Elements in a List

## Problem
Write a Python program to find the **sum of all elements** in a given list of integers.

Example

Input
```
[4, 7, 2, 9]
```

Output
```
22
```

---

# Theory

A **list** is a collection of elements.

To process each element, we iterate through the list using a loop.

General iteration pattern:

```
for element in list:
```

During iteration we accumulate the sum.

---

# Approach

1. Initialize the list
2. Initialize `total = 0`
3. Traverse the list using a loop
4. Add each element to `total`
5. Print the result

---

# Python Implementation

```python
numbers = [4, 7, 2, 9]

total = 0

for num in numbers:
    total += num

print(total)
```

---

# Key Idea

Use an **accumulator pattern**:

```
total += element
```