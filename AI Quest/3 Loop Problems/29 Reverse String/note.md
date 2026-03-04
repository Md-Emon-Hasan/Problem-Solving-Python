# Factorial Calculator

## Problem

Write a Python program using a **while loop** to calculate the factorial of a given number **N**.

Example

Input
```
5
```

Output
```
120
```

---

# Theory

The **factorial** of a number N is the product of all positive integers from **1 to N**.

Mathematically:

```
N! = N × (N-1) × (N-2) × ... × 1
```

Example:

```
5! = 5 × 4 × 3 × 2 × 1 = 120
```

Special case:

```
0! = 1
```

A **while loop** repeats execution as long as a condition is true.

---

# Approach

1. Take input `N`
2. Initialize `factorial = 1`
3. Initialize counter `i = 1`
4. Use a `while` loop until `i <= N`
5. Multiply `factorial` by `i`
6. Increment `i`
7. Print the factorial

---

# Python Implementation

```python
N = int(input())

factorial = 1
i = 1

while i <= N:
    factorial *= i
    i += 1

print(factorial)
```

---

# Key Idea

Use a **multiplicative accumulator pattern**:

```
factorial *= i
```