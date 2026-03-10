# HackerRank – Finding the Percentage

## Problem

Given student names and their marks, print the **average marks** of a specific student.

Output must show **2 decimal places**.

---

# Theory

Dictionary structure:

```
{
name : [marks]
}
```

Example:

```
{
"Krishna":[67,68,69]
}
```

Average formula:

```
sum(values) / len(values)
```

Formatting decimal:

```
{value:.2f}
```

---

# Approach

1. Store student data in dictionary
2. Retrieve marks using name
3. Calculate average
4. Print formatted result

---

# Python Implementation

```python
n = int(input())
student_marks = {}

for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()

marks = student_marks[query_name]
avg = sum(marks)/len(marks)

print(f"{avg:.2f}")
```

---

# Key Idea

Dictionary lookup:

```
dict[key]
```