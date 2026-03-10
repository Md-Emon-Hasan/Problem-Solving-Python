# HackerRank – Write a Function (Leap Year)

## Problem

Write a function `is_leap(year)` that returns:

```
True  → if the year is a leap year
False → otherwise
```

---

# Theory

Leap year rules:

1. Year divisible by 4 → leap year
2. Year divisible by 100 → not leap year
3. Year divisible by 400 → leap year

Condition:

```
(year % 4 == 0 and year % 100 != 0)
or
(year % 400 == 0)
```

---

# Approach

1. Check divisibility by 4
2. Check divisibility by 100
3. Check divisibility by 400
4. Return boolean result

---

# Python Implementation

```python
def is_leap(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True

    return False
```

---

# Key Idea

Leap year formula:

```
(year % 4 == 0 and year % 100 != 0) 
or 
(year % 400 == 0)
```