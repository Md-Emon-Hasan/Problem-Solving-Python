# Prime Number Checker

## Problem
Write a Python program to check whether a number is prime or not using a `for` loop.

If a factor is found, break out of the loop.

---

# Theory

A **prime number** is a number that has exactly two factors:

```
1 and the number itself
```

Examples:

```
2,3,5,7,11
```

A number is **not prime** if it has any divisor other than 1 and itself.

---

# Approach

1. Take number input
2. Loop from `2` to `n-1`
3. Check divisibility
4. If divisor found → break loop
5. Print result

---

# Python Implementation

```python
num = int(input())

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print("Prime")
else:
    print("Not Prime")
```

---

# Key Idea

Prime checking pattern:

```
for i in range(2,n)
    if n % i == 0
        break
```