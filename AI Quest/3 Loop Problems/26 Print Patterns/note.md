# Pattern Printing Using Nested Loops

## Problem

Write a Python program using **nested for loops** to print patterns such as:

- Right-angled triangle
- Inverted right-angled triangle

---

# Theory

Pattern printing problems use **nested loops**.

Outer loop → controls the **number of rows**

Inner loop → controls the **number of symbols per row**

General structure:

```
for row in range(...):
    for column in range(...):
        print(symbol)
```

---

# Pattern 1: Right-Angled Triangle

Output

```
*
**
***
****
*****
```

Python Code

```python
n = int(input())

for i in range(1, n+1):
    for j in range(i):
        print("*", end="")
    print()
```

---

# Pattern 2: Inverted Right-Angled Triangle

Output

```
*****
****
***
**
*
```

Python Code

```python
n = int(input())

for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
```

---

# Key Idea

Nested loop structure:

```
for row in range():
    for column in range():
```

Outer loop controls rows, inner loop controls symbols.