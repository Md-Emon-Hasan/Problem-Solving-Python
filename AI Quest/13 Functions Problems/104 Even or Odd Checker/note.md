# Even or Odd Checker Function

## Problem

Write a Python function called `even_or_odd` that takes an integer and returns:

```
"Even" → if number is even
"Odd"  → if number is odd
```

---

# Theory

An **even number** is divisible by 2.

Condition:

```
number % 2 == 0
```

An **odd number** is not divisible by 2.

Condition:

```
number % 2 != 0
```

The modulo operator `%` returns the remainder after division.

---

# Approach

1. Define function
2. Take number as parameter
3. Check divisibility by 2
4. Return appropriate result

---

# Python Implementation

```python
def even_or_odd(num):

    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


print(even_or_odd(4))
print(even_or_odd(7))
```

---

# Key Idea

Parity check pattern:

```
number % 2
```