# HackerRank – Designer Door Mat

## Problem

You are given two integers **N** and **M**.

* `N` = number of rows
* `M` = number of columns

Print the **door mat pattern** using `. | .` with the word **WELCOME** in the center.

### Rules

* `N` must be an **odd number**
* `M = 3 × N`
* The design should be **symmetrical**

---

# Example

Input

```
9 27
```

Output

```
------------.|.------------
--------.|..|..|.--------
----.|..|..|..|..|.----
.|..|..|..|..|..|..|.|
-----------WELCOME-----------
.|..|..|..|..|..|..|.|
----.|..|..|..|..|.----
--------.|..|..|.--------
------------.|.------------
```

---

# Pattern Structure

The pattern has **three sections**:

```
Top Design
WELCOME Line
Bottom Design
```

---

# Pattern Logic

### Top Pattern

The number of `. | .` patterns increases.

```
1
3
5
7
```

Example

```
.|.
.|..|..|.
.|..|..|..|..|.
```

Formula

```
".|." * i
```

Then center align it with `-`.

```
(i * ".|.").center(M, "-")
```

---

### Middle Line

Print the welcome text centered.

```
WELCOME
```

Using

```
"WELCOME".center(M, "-")
```

---

### Bottom Pattern

The bottom part is the **reverse of the top pattern**.

Sequence

```
7
5
3
1
```

---

# Algorithm

1. Read `N` and `M`
2. Print the **top pattern** using increasing sequence `1 → N`
3. Print the **WELCOME line**
4. Print the **bottom pattern** using decreasing sequence

---

# Python Implementation

```python
n, m = map(int, input().split())

# Top pattern
for i in range(1, n, 2):
    print((i * ".|.").center(m, "-"))

# Middle line
print("WELCOME".center(m, "-"))

# Bottom pattern
for i in range(n-2, -1, -2):
    print((i * ".|.").center(m, "-"))
```

---

# Key Python Concepts

### String Multiplication

```
".|." * 3
```

Output

```
.|..|..|.
```

---

### String Alignment

```
string.center(width, fillchar)
```

Example

```
"WELCOME".center(27, "-")
```

Output

```
----------WELCOME----------
```

---

### Range Function

```
range(start, stop, step)
```

Example

```
range(1, n, 2)
```

Produces

```
1, 3, 5, 7
```

---

# Time Complexity

```
O(N)
```

Because we print `N` lines.

---

# Key Insight

Most pattern printing problems follow this structure:

```
Top Pattern
Middle Line
Bottom Pattern
```

Understanding this pattern makes similar problems easier to solve.
