# GCD (Greatest Common Divisor)

## Problem

Write a Python function called `gcd` that returns the **greatest common divisor** of two integers.

Example

Input

```
12,18
```

Output

```
6
```

---

# Theory

GCD is the largest number that divides both numbers.

Efficient method: **Euclidean Algorithm**

Formula:

```
gcd(a,b) = gcd(b, a % b)
```

Stop when:

```
b = 0
```

Result:

```
GCD = a
```

---

# Approach

1. Define function
2. Use while loop
3. Update numbers using modulo
4. Return result

---

# Python Implementation

```python
def gcd(a,b):

    while b != 0:
        a, b = b, a % b

    return a


print(gcd(12,18))
print(gcd(20,30))
```

---

# Key Idea

Euclidean algorithm pattern:

```
while b != 0
    a, b = b, a % b
```