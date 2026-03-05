# List Manipulation: Sum, Average, Max, Min

## Problem

Given a list of integers, write a Python program using a **for loop** to find:

- Sum
- Average
- Maximum
- Minimum

Example

Input
```
[10, 20, 5, 30, 15]
```

Output
```
Sum = 80
Average = 16
Max = 30
Min = 5
```

---

# Theory

A **list** is a collection of elements.

To process each element in a list, we use **iteration** with a loop.

General loop pattern:

```
for item in list:
```

During iteration we can compute statistics like:

- Sum → add elements
- Average → sum / number of elements
- Maximum → largest element
- Minimum → smallest element

---

# Approach

1. Initialize variables

```
total = 0
max_val = first element
min_val = first element
```

2. Iterate through the list
3. Add each element to total
4. Update max and min
5. Compute average

---

# Python Implementation

```python
numbers = [10, 20, 5, 30, 15]

total = 0
max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    total += num
    
    if num > max_val:
        max_val = num
        
    if num < min_val:
        min_val = num

average = total / len(numbers)

print(total, average, max_val, min_val)
```

---

# Key Idea

List traversal pattern:

```
for element in list
```

with aggregation operations.