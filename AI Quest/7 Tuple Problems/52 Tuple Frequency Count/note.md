# Count Frequency of an Element in a Tuple

## Problem
Given a tuple, count how many times a **specific element** appears in the tuple.

Example

Input
```
tuple = (1, 2, 3, 2, 4, 2)
element = 2
```

Output
```
3
```

---

# Theory

To count occurrences of an element:

1. Traverse the tuple
2. Compare each element with the target
3. Increment the counter if they match

Comparison condition:

```
element == target
```

---

# Approach

1. Initialize the tuple
2. Set the target element
3. Initialize `count = 0`
4. Traverse the tuple
5. Increment count when a match is found

---

# Python Implementation

```python
t = (1, 2, 3, 2, 4, 2)

target = 2
count = 0

for item in t:
    if item == target:
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