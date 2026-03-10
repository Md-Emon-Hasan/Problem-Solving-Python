# HackerRank – Print Function

## Problem

Given an integer `n`, print the numbers from `1` to `n` without spaces.

Example

Input

```
5
```

Output

```
12345
```

---

# Theory

Python `print()` normally adds a newline.

Example:

```
print(1)
print(2)
```

Output

```
1
2
```

To avoid newline:

```
print(i, end="")
```

---

# Approach

1. Read integer `n`
2. Loop from `1 → n`
3. Print numbers without space

---

# Python Implementation

```python
n = int(input())

for i in range(1, n+1):
    print(i, end="")
```

---

# Key Idea

Print without newline:

```
end=""
```