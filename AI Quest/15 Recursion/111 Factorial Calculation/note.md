# Recursive Factorial Function

## Problem

Write a recursive Python function `factorial` that returns the factorial of a number.

Example

```
5! = 120
```

---

# Theory

Factorial definition:

```
n! = n × (n-1)!
```

Base cases:

```
0! = 1
1! = 1
```

Recursion means a function **calls itself**.

---

# Approach

1. Define function
2. Check base case
3. Call function recursively
4. Multiply result

---

# Python Implementation

```python
def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n-1)


print(factorial(5))
```

---

# Key Idea

Recursive pattern:

```
return n * function(n-1)
```