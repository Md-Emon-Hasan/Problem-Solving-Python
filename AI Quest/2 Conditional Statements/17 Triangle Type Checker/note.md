# Triangle Type Checker

## Problem

Write a Python program that takes the three sides of a triangle as input and determines whether the triangle is:

```
Equilateral
Isosceles
Scalene
```

---

# Theory

Triangles can be classified based on the equality of their sides.

Types of triangles:

### Equilateral Triangle

All three sides are equal.

```
a == b == c
```

---

### Isosceles Triangle

Two sides are equal.

```
a == b OR a == c OR b == c
```

---

### Scalene Triangle

All sides are different.

```
a != b != c
```

---

# Approach

1. Take three side lengths as input
2. Check if all sides are equal → Equilateral
3. Check if any two sides are equal → Isosceles
4. Otherwise → Scalene

---

# Python Implementation

```python
a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("Equilateral")
elif a == b or a == c or b == c:
    print("Isosceles")
else:
    print("Scalene")
```

---

# Key Idea

Triangle classification depends on **side equality conditions**:

```
a == b == c
a == b OR a == c OR b == c
else
```