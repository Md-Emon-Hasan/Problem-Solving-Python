# Leap Year Checker

## Problem

Write a Python function called `is_leap_year` that returns:

```
True  → if the year is a leap year
False → otherwise
```

---

# Theory

A leap year has **366 days**.

Leap year rules:

```
1. Year divisible by 4
2. Year not divisible by 100
3. OR divisible by 400
```

Condition:

```
(year % 4 == 0 and year % 100 != 0)
or
(year % 400 == 0)
```

---

# Approach

1. Define function
2. Apply leap year rules
3. Return boolean result

---

# Python Implementation

```python
def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


print(is_leap_year(2024))
print(is_leap_year(2023))
```

---

# Key Idea

Leap year condition:

```
(year % 4 == 0 and year % 100 != 0)
or
(year % 400 == 0)
```