# HackerRank – What's Your Name?

## Problem

Read the first name and last name of a person and print:

```
Hello firstname lastname! You just delved into python.
```

---

# Theory

Python allows formatted strings using **f-strings**.

Syntax:

```
f"text {variable}"
```

Example:

```
name = "Ross"
print(f"Hello {name}")
```

Output:

```
Hello Ross
```

---

# Approach

1. Read first name
2. Read last name
3. Format string
4. Print result

---

# Python Implementation

```python
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
```

---

# Key Idea

String formatting:

```
f"{variable}"
```