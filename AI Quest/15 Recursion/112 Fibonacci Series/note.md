# Recursive Fibonacci Function

## Problem

Write a recursive Python function `Fibonacci` that returns the **Nth Fibonacci number**.

Definition:

```
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)
```

---

# Theory

Fibonacci series is a sequence where each number is the sum of the previous two.

Example series:

```
0,1,1,2,3,5,8
```

Recursion means a function **calls itself**.

Base cases are required to stop recursion.

---

# Approach

1. Define recursive function
2. Handle base cases
3. Apply recursive formula
4. Return result

---

# Python Implementation

```python
def Fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return Fibonacci(n-1) + Fibonacci(n-2)


print(Fibonacci(6))
```

---

# Key Idea

Recursive pattern:

```
return F(n-1) + F(n-2)
```