# HackerRank – Text Alignment

## Problem

Print an `H` logo using alignment functions.

Input:

```
thickness
```

Constraints:

```
thickness must be odd
```

---

# Theory

Python string alignment functions:

```
center()
ljust()
rjust()
```

|Function|Purpose|
|---|---|
|center()|center align|
|ljust()|left align|
|rjust()|right align|

---

# Pattern Sections

The logo has 5 sections:

```
Top Cone
Top Pillars
Middle Belt
Bottom Pillars
Bottom Cone
```

---

# Python Implementation

```python
thickness = int(input())
c = 'H'

for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
```

---

# Key Idea

```
string alignment
pattern printing
```