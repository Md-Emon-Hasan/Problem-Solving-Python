# Swap Two Variables Without Temporary Variable

## Problem
Write a Python program to swap the values of two variables **without using a temporary variable**.

Example:

Input
```
a = 5
b = 10
```

Output
```
a = 10
b = 5
```

---

# Theory

Swapping means **exchanging the values of two variables**.

Normally swapping is done using a **temporary variable**.

Example:

```
temp = a
a = b
b = temp
```

But Python provides a powerful feature called **multiple assignment (tuple unpacking)**.

In this mechanism:

1. Python first creates a **tuple of values**
2. Then it **unpacks the values into variables simultaneously**

Because both operations happen in a **single atomic step**, a temporary variable is not required.

Conceptually Python does this internally:

```
a, b = (b, a)
```

So the values are swapped instantly.

---

# Approach

Use Python's **tuple unpacking** to swap variables.

Steps:

1. Store values in two variables
2. Assign them in reversed order using multiple assignment

---

# Example

```
a = 5
b = 10
```

Swap:

```
a, b = b, a
```

Result:

```
a = 10
b = 5
```

---

# Python Implementation

```python
a = 5
b = 10

a, b = b, a

print(a, b)
```

Output

```
10 5
```

---

# Key Idea

The most Pythonic way to swap two variables is:

```
a, b = b, a
```

Reason:

- Clean
- Readable
- No extra variable
- Constant time operation