# Leap Year Checker

## Problem
Write a Python program that takes a year as input and determines whether it is a **leap year or not**.

Example

Input
```
2024
```

Output
```
Leap Year
```

---

# Theory

A **leap year** has **366 days** instead of 365 days.  
In a leap year, February has **29 days**.

Leap year rules:

1. If a year is divisible by **400**, it is a leap year.

```
year % 400 == 0
```

2. If a year is divisible by **4** but **not divisible by 100**, it is also a leap year.

```
year % 4 == 0 and year % 100 != 0
```

Otherwise, it is **not a leap year**.

---

# Approach

1. Take the year as input
2. Check if it is divisible by **400**
3. Otherwise check if it is divisible by **4 but not by 100**
4. Print the result

---

# Python Implementation

```python
year = int(input())

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
```

---

# Key Idea

Leap year condition:

```
year % 400 == 0
OR
year % 4 == 0 and year % 100 != 0
```