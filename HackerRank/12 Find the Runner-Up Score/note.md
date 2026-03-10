# HackerRank – Find the Runner-Up Score

## Problem

Given a list of scores, find the **second highest score**.

Example

Input

```
5
2 3 6 6 5
```

Output

```
5
```

---

# Theory

Runner-up score means:

```
Second largest unique number
```

Steps:

1. Remove duplicate values
2. Sort numbers
3. Select second largest

---

# Approach

1. Convert input to list
2. Remove duplicates using `set`
3. Sort list
4. Print second last element

---

# Python Implementation

```python
n = int(input())
arr = list(map(int, input().split()))

unique_scores = list(set(arr))
unique_scores.sort()

print(unique_scores[-2])
```

---

# Key Idea

Remove duplicates:

```
set()
```

Second largest:

```
list[-2]
```