# List Sum Calculator

## Problem

Write a Python function called `list_sum` that takes a **list of integers** and returns the **sum of all elements**.

Example

Input
```
[1,2,3,4]
```

Output
```
10
```

---

# Theory

A list contains multiple elements.

To process all elements we use a **loop**.

To accumulate values we use a **running sum variable**.

Pattern:

```
total += element
```

---

# Approach

1. Define function `list_sum(numbers)`
2. Initialize `total = 0`
3. Traverse list using `for`
4. Add each element to total
5. Return result

---

# Python Implementation

```python
def list_sum(numbers):

    total = 0

    for num in numbers:
        total += num

    return total


print(list_sum([1,2,3,4]))
```

---

# Key Idea

Accumulation pattern:

```
total = 0

for element in list:
    total += element
```