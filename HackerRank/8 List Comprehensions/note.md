# HackerRank – List Comprehensions

## Problem

Given integers `x, y, z, n`, print a list of coordinates:

```
[i, j, k]
```

Where:

```
0 ≤ i ≤ x
0 ≤ j ≤ y
0 ≤ k ≤ z
```

Condition:

```
i + j + k ≠ n
```

---

# Theory

List comprehension allows creating lists using loops in a single line.

Structure:

```
[expression for item in iterable if condition]
```

---

# Approach

1. Loop `i` from `0 → x`
2. Loop `j` from `0 → y`
3. Loop `k` from `0 → z`
4. Keep only elements where `i + j + k != n`

---

# Python Implementation

```python
x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i,j,k]
          for i in range(x+1)
          for j in range(y+1)
          for k in range(z+1)
          if i+j+k != n]

print(result)
```

---

# Key Idea

Nested list comprehension:

```
for i
 for j
  for k
```