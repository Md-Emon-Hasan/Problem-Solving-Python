# Typecasting Challenge

## Problem

Given three variables:

```
a = "100"
b = 25
c = "10.5"
```

Perform the following operations:

1. Convert `a` to an integer and add it to `b`
2. Convert `c` to a float and subtract it from the result of the first operation
3. Convert the final result to a string and concatenate it with `" is the answer."`

---

# Theory

**Typecasting (Type Conversion)** means converting a value from one data type to another.

Common Python type conversion functions:

```
int()   → convert to integer
float() → convert to float
str()   → convert to string
```

This problem demonstrates how to perform arithmetic operations after converting data types.

---

# Approach

1. Convert `a` from string to integer using `int()`
2. Add it with `b`
3. Convert `c` from string to float using `float()`
4. Subtract it from the previous result
5. Convert the final result to string using `str()`
6. Concatenate it with the message `" is the answer."`

---

# Python Implementation

```python
a = "100"
b = 25
c = "10.5"

result1 = int(a) + b
result2 = result1 - float(c)

final_result = str(result2) + " is the answer."

print(final_result)
```

Output

```
114.5 is the answer.
```

---

# Key Idea

Use Python type conversion functions:

```
int()
float()
str()
```

to perform operations between different data types.