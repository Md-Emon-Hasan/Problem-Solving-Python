# Average of Elements in a List

## Problem
Write a Python program to calculate the **average of all elements** in a given list of integers.

Example

Input
```
[10, 20, 30, 40]
```

Output
```
25
```

---

# Theory

The **average** of numbers is calculated using the formula:

```
Average = Sum of elements / Number of elements
```

To compute the sum of elements in a list, we iterate through the list using a loop.

General iteration pattern:

```
for element in list:
```

---

# Approach

1. Initialize the list
2. Initialize `total = 0`
3. Traverse the list using a loop
4. Add each element to `total`
5. Compute average

```
average = total / len(list)
```

---

# Python Implementation

```python
numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print(average)
```

---

# Key Idea

Aggregation pattern:

```
total += element
average = total / count
```