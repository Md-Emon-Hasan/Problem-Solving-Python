# HackerRank – Text Wrap

## Problem

Wrap a long string into lines of width `w`.

Example

Input

```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
4
```

Output

```
ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
```

---

# Theory

Python provides a module called:

```
textwrap
```

Function:

```
textwrap.fill(text, width)
```

This breaks the text into multiple lines.

---

# Approach

1. Import `textwrap`
2. Use `textwrap.fill`
3. Return the wrapped string

---

# Python Implementation

```python
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)
```

---

# Key Idea

```
textwrap.fill()
```