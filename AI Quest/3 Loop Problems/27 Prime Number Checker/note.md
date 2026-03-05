# Prime Number Checker (Using For Loop)

## Problem
Write a Python program using a **for loop** to check whether a given number **N** is prime or not.

Example

Input
```
7
```

Output
```
Prime
```

---

# Theory

A **prime number** is a number greater than **1** that has only two divisors:

```
1 and itself
```

Examples

```
2, 3, 5, 7, 11
```

A number is **not prime** if it is divisible by any number between **2 and N-1**.

Divisibility rule

```
N % i == 0
```

---

# Approach

1. Take integer input `N`
2. Assume the number is prime
3. Use a `for` loop from `2` to `N-1`
4. If any number divides `N`, it is not prime
5. Otherwise it is prime

---

# Python Implementation

```python
N = int(input())

is_prime = True

for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break

if is_prime and N > 1:
    print("Prime")
else:
    print("Not Prime")
```

---

# Key Idea

Check divisibility using:

```
N % i == 0
```

inside a loop.