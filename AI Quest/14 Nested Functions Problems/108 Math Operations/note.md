# Math Operations using Nested Functions

## Problem

Write a function `math_operations` that performs mathematical operations on three numbers.

Operations supported:

```
add
subtract
multiply
divide
```

Use **nested functions** to implement each operation.

---

# Theory

A **nested function** is a function defined inside another function.

Example:

```
def outer():
    def inner():
        pass
```

Nested functions are useful for:

```
code organization
encapsulation
logic grouping
```

---

# Approach

1. Define main function
2. Create nested functions for operations
3. Check operation string
4. Call appropriate function
5. Return result

---

# Python Implementation

```python
def math_operations(a,b,c,operation):

    def add():
        return a+b+c

    def subtract():
        return a-b-c

    def multiply():
        return a*b*c

    def divide():
        return a/b/c

    if operation == "add":
        return add()

    elif operation == "subtract":
        return subtract()

    elif operation == "multiply":
        return multiply()

    elif operation == "divide":
        return divide()
```

---

# Key Idea

Nested function structure:

```
def outer():
    def inner():
        pass
```