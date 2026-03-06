# Convert List of Coordinate Tuples into X and Y Lists

## Problem
Given a list containing tuples of `(x, y)` coordinates, create two separate lists:
- one containing all **x-coordinates**
- one containing all **y-coordinates**

Example

Input
```
[(1,2),(3,4),(5,6)]
```

Output
```
x_list = [1,3,5]
y_list = [2,4,6]
```

---

# Theory

Each tuple contains two values:

```
(x, y)
```

We can use **tuple unpacking** to extract them.

Example:

```
for x, y in coordinates
```

This automatically assigns:

```
x → first value
y → second value
```

---

# Approach

1. Initialize the list of tuples
2. Create two empty lists
3. Traverse the coordinate list
4. Unpack each tuple
5. Append values to corresponding lists

---

# Python Implementation

```python
coordinates = [(1,2),(3,4),(5,6)]

x_list = []
y_list = []

for x, y in coordinates:
    x_list.append(x)
    y_list.append(y)

print(x_list)
print(y_list)
```

---

# Key Idea

Tuple unpacking pattern:

```
for x, y in data
```