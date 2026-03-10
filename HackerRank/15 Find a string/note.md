# HackerRank – Find a String

## Problem

Given a string and a substring, count how many times the substring occurs in the string.

Overlapping matches must also be counted.

Example

Input

```
ABCDCDC
CDC
```

Output

```
2
```

---

# Theory

To find overlapping occurrences, we must manually traverse the string.

Use slicing:

```
string[i:i+len(substring)]
```

---

# Approach

1. Traverse the string
2. Extract substring using slicing
3. Compare with target substring
4. Increment counter if match found

---

# Python Implementation

```python
def count_substring(string, sub_string):
    count = 0

    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            count += 1

    return count
```

---

# Key Idea

Substring slicing:

```
string[i:i+k]
```