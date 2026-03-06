# Tuple Membership Test

## Problem
Write a Python program that takes an element as input and checks if it exists in a given tuple.

Example

Input
```
tuple = (10, 20, 30, 40)
element = 20
```

Output
```
Element exists in the tuple
```

---

# Theory

Membership testing checks whether an element exists inside a sequence.

Python uses the **`in` operator**.

Syntax:

```
element in tuple
```

Returns:

```
True / False
```

---

# Approach

1. Initialize the tuple
2. Take input from the user
3. Use the `in` operator to check membership
4. Print the result

---

# Python Implementation

```python
t = (10, 20, 30, 40)

element = int(input())

if element in t:
    print("Element exists")
else:
    print("Element not found")
```

---

# Key Idea

Membership operator:

```
value in sequence
```