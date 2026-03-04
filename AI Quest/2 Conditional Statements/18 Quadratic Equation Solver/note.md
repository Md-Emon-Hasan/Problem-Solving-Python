# Quadratic Equation Solver

## Problem

Write a Python program that takes coefficients **a, b, c** of a quadratic equation and calculates the roots.

Quadratic equation form:

```
ax² + bx + c = 0
```

The program should print:

- Real roots if they exist
- A message if the roots are complex

---

# Theory

The roots of a quadratic equation are calculated using the **quadratic formula**:

```
x = (-b ± √(b² - 4ac)) / (2a)
```

The expression

```
D = b² - 4ac
```

is called the **discriminant**.

---

# Discriminant Cases

```
D > 0 → two real and distinct roots
D = 0 → two real and equal roots
D < 0 → complex roots
```

---

# Approach

1. Take inputs `a`, `b`, `c`
2. Calculate the discriminant

```
D = b² - 4ac
```

3. Use conditional statements to determine root type
4. Calculate and print the roots

---

# Python Implementation

```python
import math

a = float(input())
b = float(input())
c = float(input())

D = b**2 - 4*a*c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2*a)
    root2 = (-b - math.sqrt(D)) / (2*a)
    print(root1, root2)

elif D == 0:
    root = -b / (2*a)
    print(root)

else:
    print("Complex roots")
```

---

# Key Idea

Use the **discriminant**:

```
D = b² - 4ac
```

to determine the nature of the roots.