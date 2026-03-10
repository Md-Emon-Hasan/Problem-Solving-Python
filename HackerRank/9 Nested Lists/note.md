# HackerRank – Nested Lists

## Problem

Given student names and scores, print the names of students having the **second lowest score**.

If multiple students have that score:

```
print names alphabetically
```

---

# Theory

Steps:

1. Store student data in nested list
2. Extract unique scores
3. Sort scores
4. Find second lowest score
5. Print students with that score

---

# Approach

1. Create list `students`
2. Extract scores
3. Remove duplicates using `set`
4. Sort scores
5. Select second score
6. Print matching names

---

# Python Implementation

```python
students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = sorted(set([score for name, score in students]))

second = scores[1]

names = [name for name, score in students if score == second]

for name in sorted(names):
    print(name)
```

---

# Key Idea

Nested list structure:

```
[name, score]
```