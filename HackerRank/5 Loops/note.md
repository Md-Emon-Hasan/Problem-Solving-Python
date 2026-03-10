# HackerRank – Python Loops

## Problem

Given an integer `n`, print the square of all non-negative integers less than `n`.

Example

Input

```
5
```

Output

```
0
1
4
9
16
```

---

# Theory

Python loop:

```
for i in range(n)
```

Range generates numbers:

```
0 → n-1
```

Square formula:

```
i² = i * i
```

---

# Approach

1. Read integer `n`
2. Loop from `0 → n-1`
3. Print square of each number

---

# Python Implementation

```python
n = int(input())

for i in range(n):
    print(i*i)
```

---

# Key Idea

Loop pattern:

```
for i in range(n)
```