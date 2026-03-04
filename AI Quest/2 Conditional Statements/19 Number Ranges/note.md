# Number Range Classification

## Problem

Write a Python program that takes an integer as input and determines which range the number belongs to:

```
0–50
51–100
101–150
Above 150
```

---

# Theory

This problem demonstrates **range-based classification** using conditional statements.

A number can be checked against ranges using comparison operators.

Python allows a clean syntax for range checking:

```
lower_bound <= value <= upper_bound
```

Example:

```
0 <= x <= 50
```

---

# Approach

1. Take an integer input
2. Check if the number is between **0 and 50**
3. Check if the number is between **51 and 100**
4. Check if the number is between **101 and 150**
5. Otherwise the number is **above 150**

---

# Python Implementation

```python
num = int(input())

if 0 <= num <= 50:
    print("0-50")
elif 51 <= num <= 100:
    print("51-100")
elif 101 <= num <= 150:
    print("101-150")
else:
    print("Above 150")
```

---

# Key Idea

Use **range comparison pattern**:

```
lower_bound <= value <= upper_bound
```