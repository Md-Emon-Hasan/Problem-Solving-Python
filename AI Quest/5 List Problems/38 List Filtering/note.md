# List Filtering (Even Numbers)

## Problem
Given a list of integers, create a new list that contains **only the even numbers** from the original list.

Example

Input
```
[1, 2, 3, 4, 5, 6]
```

Output
```
[2, 4, 6]
```

---

# Theory

An **even number** is divisible by **2**.

Condition:

```
number % 2 == 0
```

Filtering means selecting elements that satisfy a condition.

---

# Approach

1. Initialize the original list
2. Create an empty list
3. Traverse the list using a loop
4. Check if the element is even
5. Add it to the new list

---

# Python Implementation

```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print(even_numbers)
```

---

# Key Idea

Filtering pattern:

```
if condition:
    new_list.append(element)
```