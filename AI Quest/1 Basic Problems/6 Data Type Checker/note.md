# Data Type Checker

## Problem
Write a Python function that takes a variable as input and returns the **data type of the variable as a string**.

Example

Input
```
10
```

Output
```
int
```

---

# Theory

In Python, every value has a **data type** that defines what kind of data it represents.

Examples:

```
10      → int
3.14    → float
"hello" → str
[1,2,3] → list
True    → bool
```

Python provides a built-in function called `type()` that returns the type of a variable.

Example

```
type(10)
```

Output

```
<class 'int'>
```

To get only the type name as a string, we use:

```
type(variable).__name__
```

---

# Approach

1. Take a variable as input
2. Use `type()` to determine its data type
3. Access the type name using `__name__`
4. Return it as a string

---

# Python Implementation

```python
def get_data_type(value):
    return type(value).__name__
```

Example

```python
print(get_data_type(10))
print(get_data_type("hello"))
```

Output

```
int
str
```

---

# Key Idea

Use Python's built-in function:

```
type(variable).__name__
```

to get the **data type name as a string**.