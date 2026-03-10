# HackerRank – itertools.product()

## Problem

You are given two lists:

```
A
B
```

Compute their **Cartesian Product A × B**.

---

# Example

Input

```
1 2
3 4
```

Output

```
(1, 3) (1, 4) (2, 3) (2, 4)
```

---

# Cartesian Product Concept

Cartesian product creates all possible pairs:

```
(A element , B element)
```

Example

```
A = [1,2]
B = [3,4]
```

Result

```
(1,3)
(1,4)
(2,3)
(2,4)
```

---

# Python Tool

Python provides:

```
itertools.product()
```

---

# Implementation

```python
from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = list(product(A, B))

for i in result:
    print(i, end=" ")
```

---

# Alternative Logic (Without itertools)

Nested loop:

```python
for a in A:
    for b in B:
        print((a,b), end=" ")
```

---

# Complexity

```
Time  : O(n × m)
Space : O(n × m)
```

Where

```
n = len(A)
m = len(B)
```
