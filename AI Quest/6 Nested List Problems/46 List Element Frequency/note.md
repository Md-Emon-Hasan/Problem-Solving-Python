# Frequency Count in a Nested List

## Problem
Given a nested list of integers, count the **frequency of each element** in the entire list.

Example

Input
```
[[1,2,3],[2,3,4],[1,2]]
```

Output
```
1 : 2
2 : 3
3 : 2
4 : 1
```

---

# Theory

A nested list contains lists as elements.

Example:

```
[[1,2],[3,4]]
```

To count element frequency:

1. Traverse each sublist
2. Traverse each element
3. Store counts using a dictionary

Dictionary structure:

```
element → frequency
```

---

# Approach

1. Initialize nested list
2. Create an empty dictionary
3. Traverse nested list
4. Update counts for each element

---

# Python Implementation

```python
nested_list = [[1,2,3],[2,3,4],[1,2]]

frequency = {}

for sublist in nested_list:
    for num in sublist:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

print(frequency)
```

---

# Key Idea

Nested traversal + counting pattern:

```
for sublist in nested_list
    for element in sublist
        count[element] += 1
```