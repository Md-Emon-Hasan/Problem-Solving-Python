# Element-wise Tuple Operations

## Problem
Given two tuples of integers, perform element-wise **addition, subtraction, and multiplication** and create new tuples for each operation.

Example

Input
```
t1 = (1, 2, 3)
t2 = (4, 5, 6)
```

Output
```
Addition       → (5, 7, 9)
Subtraction    → (-3, -3, -3)
Multiplication → (4, 10, 18)
```

---

# Theory

Element-wise operations apply arithmetic operations on elements at the **same index**.

For index `i`:

```
result[i] = t1[i] operation t2[i]
```

Example:

```
(1+4, 2+5, 3+6)
```

---

# Approach

1. Initialize two tuples
2. Create empty tuples for results
3. Traverse tuples using index
4. Perform arithmetic operations
5. Store results in new tuples

---

# Python Implementation

```python
t1 = (1, 2, 3)
t2 = (4, 5, 6)

add = ()
sub = ()
mul = ()

for i in range(len(t1)):
    add += (t1[i] + t2[i],)
    sub += (t1[i] - t2[i],)
    mul += (t1[i] * t2[i],)

print(add, sub, mul)
```

---

# Key Idea

Element-wise operation pattern:

```
result[i] = a[i] op b[i]
```