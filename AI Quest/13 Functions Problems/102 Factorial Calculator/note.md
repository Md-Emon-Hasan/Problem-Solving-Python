# Factorial Function

## Problem

Write a Python function called `factorial` that takes an integer and returns its factorial.

---

# Theory

Factorial of a number is defined as:

```
n! = n × (n-1) × ... × 1
```

Examples:

```
3! = 6
5! = 120
```

---

# Approach

1. Create function `factorial(n)`
2. Initialize result = 1
3. Loop from `1 → n`
4. Multiply each number
5. Return result

---

# Python Implementation

```python
def factorial(n):
    result = 1

    for i in range(1,n+1):
        result *= i

    return result


print(factorial(3))
print(factorial(5))
```

---

# Key Idea

Multiplication accumulation pattern:

```
result = 1
for i in range(1,n+1):
    result *= i
```