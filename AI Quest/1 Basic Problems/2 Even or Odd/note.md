# Even or Odd Number

## Problem
Write a Python program that takes an integer as input and prints whether it is **even or odd**.

Example

Input
```
7
```

Output
```
Odd
```

---

# Theory

Numbers can be classified into two categories:

### Even Number
A number is even if it is divisible by **2** with **no remainder**.

Example:
```
2, 4, 6, 8
```

Mathematically:

```
n % 2 = 0
```

---

### Odd Number

A number is odd if it is **not divisible by 2**.

Example:
```
1, 3, 5, 7
```

Mathematically:

```
n % 2 ≠ 0
```

---

# Approach

To determine whether a number is even or odd:

1. Take an integer input
2. Use the **modulus operator `%`**
3. Check the remainder when dividing by **2**

Rules:

```
number % 2 == 0 → Even
number % 2 != 0 → Odd
```

---

# Python Implementation

```python
num = int(input("Enter an integer: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

# Key Idea

The modulus operator `%` returns the remainder of a division.

So:

```
n % 2 == 0 → Even
n % 2 != 0 → Odd
```