# Greeting Generator (Nested Functions)

## Problem

Write a Python function `greeting_generator` that takes a name and returns a greeting message.

Example output:

```
Hello, Emon! How are you today?
```

Use **nested functions**.

---

# Theory

A **nested function** is a function defined inside another function.

Example:

```
def outer():

    def inner():
        pass
```

Nested functions help organize logic and hide helper functions.

Python **f-strings** allow easy string formatting:

```
f"Hello {name}"
```

---

# Approach

1. Define main function
2. Create nested function
3. Generate greeting message
4. Return message

---

# Python Implementation

```python
def greeting_generator(name):

    def create_greeting():
        return f"Hello, {name}! How are you today?"

    return create_greeting()


print(greeting_generator("Emon"))
print(greeting_generator("Alice"))
```

---

# Key Idea

Nested function pattern:

```
def outer():
    def inner():
        pass
```