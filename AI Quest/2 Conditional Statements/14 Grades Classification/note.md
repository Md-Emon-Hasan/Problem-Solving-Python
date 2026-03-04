# Grades Classification

## Problem

Write a Python program that takes a student's **percentage** as input and prints the corresponding **grade**.

Grade criteria:

```
90% or above → A+
80–89%       → A
70–79%       → B
60–69%       → C
Below 60%    → Fail
```

---

# Theory

This problem demonstrates **range-based conditional logic**.

The percentage is compared against different ranges to determine the grade.

Python uses **if-elif-else** statements to check multiple conditions sequentially.

To avoid incorrect classification, conditions should be checked **from highest range to lowest range**.

---

# Approach

1. Take the percentage as input
2. Check if percentage ≥ 90 → A+
3. Else check if percentage ≥ 80 → A
4. Else check if percentage ≥ 70 → B
5. Else check if percentage ≥ 60 → C
6. Otherwise → Fail

---

# Python Implementation

```python
percentage = float(input())

if percentage >= 90:
    print("A+")
elif percentage >= 80:
    print("A")
elif percentage >= 70:
    print("B")
elif percentage >= 60:
    print("C")
else:
    print("Fail")
```

---

# Key Idea

Use **range checking with if-elif-else**:

```
≥ 90
≥ 80
≥ 70
≥ 60
else
```