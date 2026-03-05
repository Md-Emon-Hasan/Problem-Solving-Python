# Common Elements Between Two Lists

## Problem
Given two lists of integers, create a new list containing elements that are **common to both lists**.

Example

Input
```
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
```

Output
```
[3, 4]
```

---

# Theory

To find common elements between two lists:

1. Traverse one list
2. Check if each element exists in the second list
3. Collect matching elements

Membership check:

```
element in list
```

---

# Approach

1. Initialize two lists
2. Create an empty list for results
3. Traverse the first list
4. Check if the element exists in the second list
5. Append it to the result list

---

# Python Implementation

```python
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print(common)
```

---

# Key Idea

Membership checking:

```
if element in list
```