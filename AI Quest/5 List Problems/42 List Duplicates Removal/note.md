# Remove Duplicates from a List (Preserving Order)

## Problem
Write a Python program to remove duplicate elements from a list while **preserving the original order**.

Example

Input
```
[1, 2, 2, 3, 4, 3, 5]
```

Output
```
[1, 2, 3, 4, 5]
```

---

# Theory

Duplicate removal means keeping only **one occurrence** of each element.

To preserve order:

1. Traverse the original list
2. Add elements to a new list only if they are not already present

Membership check:

```
element not in list
```

---

# Approach

1. Initialize the list
2. Create an empty result list
3. Traverse the original list
4. Check if the element exists in the result list
5. Append it if not present

---

# Python Implementation

```python
numbers = [1, 2, 2, 3, 4, 3, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print(result)
```

---

# Key Idea

Duplicate filtering pattern:

```
if element not in result:
    result.append(element)
```