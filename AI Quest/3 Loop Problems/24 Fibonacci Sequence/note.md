# Fibonacci Sequence Generator

## Problem
Write a Python program using a **for loop** to generate the **Fibonacci sequence** up to a given limit **N**.

Example

Input
```
7
```

Output
```
0 1 1 2 3 5 8
```

---

# Theory

The Fibonacci sequence is a series where each number is the **sum of the two preceding numbers**.

Formula:

```
F(n) = F(n-1) + F(n-2)
```

Sequence starts with:

```
0, 1
```

Example sequence:

```
0 1 1 2 3 5 8 13
```

---

# Approach

1. Take integer input `N`
2. Initialize two variables

```
a = 0
b = 1
```

3. Use a `for` loop to generate numbers
4. Print the current value
5. Update values using

```
a, b = b, a + b
```

---

# Python Implementation

```python
N = int(input())

a, b = 0, 1

for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
```

---

# Key Idea

Use the Fibonacci update rule:

```
a, b = b, a + b
```