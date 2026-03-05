# Sum of Even Numbers (1 to N)

## Problem

Write a Python program using a **while loop** to calculate the sum of all **even numbers between 1 and N**, where **N is taken as input** from the user.

Example

Input
```
10
```

Output
```
30
```

---

# Theory

An **even number** is a number divisible by **2**.

Condition:

```
number % 2 == 0
```

Example even numbers:

```
2, 4, 6, 8, 10
```

To calculate the sum, we iterate through numbers from **1 to N** and add only the even numbers.

---

# Approach

1. Take input `N`
2. Initialize `total = 0`
3. Initialize counter `i = 1`
4. Use a `while` loop until `i <= N`
5. Check if `i` is even
6. Add it to the sum
7. Increment `i`

---

# Python Implementation

```python
N = int(input())

total = 0
i = 1

while i <= N:
    if i % 2 == 0:
        total += i
    i += 1

print(total)
```

---

# Key Idea

Filter even numbers using:

```
i % 2 == 0
```

and accumulate using:

```
total += i
```