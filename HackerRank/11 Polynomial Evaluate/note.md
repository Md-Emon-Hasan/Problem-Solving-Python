# HackerRank – Numpy Polynomials

## Problem

Evaluate a polynomial at a given value.

Input:

```
coefficients
x
```

Output:

```
P(x)
```

---

# Theory

Polynomial form:

```
P(x) = a₀xⁿ + a₁xⁿ⁻¹ + ... + aₙ
```

Numpy function:

```
numpy.polyval(coefficients, x)
```

---

# Approach

1. Read polynomial coefficients
2. Read value `x`
3. Use `numpy.polyval`
4. Print result

---

# Python Implementation

```python
import numpy

coefficients = list(map(float, input().split()))
x = float(input())

print(numpy.polyval(coefficients, x))
```

---

# Key Idea

Polynomial evaluation:

```
numpy.polyval()
```