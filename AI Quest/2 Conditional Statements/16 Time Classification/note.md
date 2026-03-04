# Time Classification

## Problem

Write a Python program that takes time in **hours (24-hour format)** as input and prints an appropriate greeting.

Example

Input
```
9
```

Output
```
Good Morning
```

---

# Theory

In the **24-hour time format**, hours range from:

```
0 → 23
```

We classify the time of day into different categories using **range conditions**.

Example classification:

```
5 – 11  → Good Morning
12 – 16 → Good Afternoon
17 – 20 → Good Evening
Else    → Good Night
```

This can be implemented using **if-elif-else conditional statements**.

---

# Approach

1. Take the hour as input
2. Check if hour is between **5 and 11**
3. Check if hour is between **12 and 16**
4. Check if hour is between **17 and 20**
5. Otherwise print **Good Night**

---

# Python Implementation

```python
hour = int(input())

if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 16:
    print("Good Afternoon")
elif 17 <= hour <= 20:
    print("Good Evening")
else:
    print("Good Night")
```

---

# Key Idea

Use **range checking** with conditional statements:

```
5 <= hour <= 11
12 <= hour <= 16
17 <= hour <= 20
else → night
```