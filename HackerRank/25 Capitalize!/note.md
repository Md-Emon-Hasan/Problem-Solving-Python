# HackerRank – Capitalize!

## Problem

Given a string **S** containing a full name, capitalize the first letter of every word.

Example

Input

```
chris alan
```

Output

```
Chris Alan
```

---

# Key Idea

For each word:

```
first_letter → uppercase
rest_of_word → unchanged
```

---

# Important Detail

The string may contain **multiple spaces**, so we must use:

```
split(" ")
```

instead of

```
split()
```

---

# Algorithm

1. Read input string `s`
2. Split string into words using `" ".split`
3. For each word:

   * Convert first character to uppercase
   * Keep remaining characters unchanged
4. Join words back using `" ".join`

---

# Python Implementation

```python
def solve(s):

    words = s.split(" ")
    result = []

    for w in words:

        if w:
            result.append(w[0].upper() + w[1:])
        else:
            result.append(w)

    return " ".join(result)
```

---

# Example

Input

```
hello world
```

Processing

```
hello → Hello
world → World
```

Output

```
Hello World
```

---

# Complexity

```
Time  : O(n)
Space : O(n)
```

---

# Trick to Remember

```
word[0].upper() + word[1:]
```

This converts only the **first letter** to uppercase.
