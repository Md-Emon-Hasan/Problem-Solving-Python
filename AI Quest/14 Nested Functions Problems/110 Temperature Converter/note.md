# Temperature Converter (Nested Functions)

## Problem

Write a Python function `temperature_converter` that converts temperature between **Celsius and Fahrenheit**.

Inputs:

```
temperature
scale ("C" or "F")
```

Output:

Converted temperature.

---

# Theory

Temperature conversion formulas:

Celsius → Fahrenheit

```
F = (C × 9/5) + 32
```

Fahrenheit → Celsius

```
C = (F − 32) × 5/9
```

Nested functions allow helper logic to be defined inside another function.

---

# Approach

1. Define main function
2. Create nested functions for conversion
3. Check scale
4. Call appropriate conversion function
5. Return result

---

# Python Implementation

```python
def temperature_converter(temp, scale):

    def c_to_f():
        return (temp * 9/5) + 32

    def f_to_c():
        return (temp - 32) * 5/9

    if scale == "C":
        return c_to_f()

    elif scale == "F":
        return f_to_c()
```

---

# Key Idea

Nested helper functions:

```
def outer():
    def helper():
        pass
```