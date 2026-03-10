# HackerRank – Alphabet Rangoli

## Problem

Print an **alphabet rangoli pattern** of size `n`.

The rangoli should contain:

```
alphabet pattern
hyphen separators
center alignment
symmetrical structure
```

---

# Example

Input

```
5
```

Output

```
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

---

# Key Observations

```
1️⃣ Rangoli is symmetrical
2️⃣ Middle line contains full alphabet sequence
3️⃣ Width = 4*n - 3
```

---

# Width Formula

```
width = 4 * n - 3
```

Example

```
n = 5
width = 17
```

---

# Alphabet Source

Python provides:

```
string.ascii_lowercase
```

Result

```
abcdefghijklmnopqrstuvwxyz
```

---

# Pattern Generation

For each row:

```
left_part  = reversed letters
right_part = forward letters
```

Example

```
e-d-c-b-a-b-c-d-e
```

---

# Joining Letters

```
"-".join(letters)
```

Example

```
["e","d","c"]
```

becomes

```
e-d-c
```

---

# Alignment

```
string.center(width, "-")
```

Example

```
----e-d-c-d-e----
```

---

# Symmetry Trick

```
top = lines[:0:-1]
bottom = lines
```

Final pattern

```
top + bottom
```

---

# Python Implementation

```python
import string

def print_rangoli(size):

    alpha = string.ascii_lowercase
    width = 4 * size - 3

    lines = []

    for i in range(size):

        left = alpha[size-1:i:-1]
        right = alpha[i:size]

        row = "-".join(left + right)

        lines.append(row.center(width, "-"))

    print("\n".join(lines[:0:-1] + lines))
```

---

# Complexity

```
Time  : O(n²)
Space : O(n²)
```

---

# Pattern Solving Trick

Almost all pattern problems follow:

```
Top
Middle
Bottom
```

This rangoli follows the same principle.
