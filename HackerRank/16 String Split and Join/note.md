# HackerRank – String Split and Join

## Problem

Given a string of space-separated words, split the string and join it using a hyphen (`-`).

Example

Input

```
this is a string
```

Output

```
this-is-a-string
```

---

# Theory

Python provides two useful string functions:

### split()

Splits a string into a list.

```
string.split(delimiter)
```

Example:

```
"hello world".split(" ")
→ ['hello','world']
```

### join()

Joins elements of a list into a string.

```
delimiter.join(list)
```

Example:

```
"-".join(['hello','world'])
→ hello-world
```

---

# Approach

1. Split the string by space
2. Join using hyphen

---

# Python Implementation

```python
def split_and_join(line):
    words = line.split(" ")
    return "-".join(words)
```

---

# Key Idea

```
split() + join()
```