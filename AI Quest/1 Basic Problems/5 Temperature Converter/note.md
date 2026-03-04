# Temperature Converter (Celsius → Fahrenheit)

## Problem
Write a Python program that converts a temperature in **Celsius to Fahrenheit**.  
Take the Celsius temperature as input from the user.

Example

Input
```
25
```

Output
```
77.0
```

---

# Theory

Temperature can be measured in different scales such as:

- Celsius (°C)
- Fahrenheit (°F)

The relationship between Celsius and Fahrenheit is defined by the formula:

```
F = (C × 9/5) + 32
```

Where:

```
C = Celsius
F = Fahrenheit
```

This formula converts a Celsius temperature into Fahrenheit.

---

# Approach

1. Take temperature input in Celsius
2. Apply the conversion formula
3. Print the Fahrenheit value

---

# Python Implementation

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)
```

---

# Key Idea

Use the conversion formula:

```
F = (C × 9/5) + 32
```