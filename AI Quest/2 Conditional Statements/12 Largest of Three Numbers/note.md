# Largest of Three Numbers

## Problem
Write a Python program that takes three numbers as input and prints the **largest among them**.

Example

Input
```
5
10
7
```

Output
```
10
```

---

# Theory

To determine the largest among three numbers, we compare the numbers using **conditional statements**.

If:

```
a ≥ b and a ≥ c
```

then `a` is the largest.

If:

```
b ≥ a and b ≥ c
```

then `b` is the largest.

Otherwise:

```
c` is the largest.
```

Python uses logical operators like:

```
and
```

to combine multiple conditions.

---

# Approach

1. Take three numbers as input
2. Compare them using `if-elif-else`
3. Determine which number is greater than the others
4. Print the largest number

---

# Python Implementation

```python
a = float(input())
b = float(input())
c = float(input())

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(largest)
```

---

# Key Idea

Use conditional comparisons:

```
a ≥ b and a ≥ c
b ≥ a and b ≥ c
```

to determine the largest value.