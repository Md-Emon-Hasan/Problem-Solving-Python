# HackerRank – Python If-Else

## Problem

Given an integer `n`, print:

- "Weird" if `n` is odd
- "Not Weird" if `n` is even and between `2–5`
- "Weird" if `n` is even and between `6–20`
- "Not Weird" if `n` is even and greater than `20`

---

# Theory

Odd number condition:

```
n % 2 != 0
```

Even number condition:

```
n % 2 == 0
```

Python supports **range checking**:

```
2 <= n <= 5
```

---

# Python Implementation

```python
n = int(input())

if n % 2 != 0:
    print("Weird")

elif 2 <= n <= 5:
    print("Not Weird")

elif 6 <= n <= 20:
    print("Weird")

else:
    print("Not Weird")
```

---

# Key Idea

Conditional pattern:

```
if
elif
else
```