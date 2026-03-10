# HackerRank – String Formatting

## Problem

Given an integer **n**, print numbers from **1 → n** in four formats:

```
Decimal
Octal
Hexadecimal (uppercase)
Binary
```

All values must be **right aligned** with the width of the **binary representation of n**.

---

# Example

Input

```
5
```

Output

```
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
```

---

# Key Idea

Alignment width = binary length of **n**

```
width = len(bin(n)) - 2
```

Because:

```
bin(n) -> 0b10101
```

`0b` is removed.

---

# Number System Conversion

Python built-in functions:

```
bin(x)
oct(x)
hex(x)
```

Example

```
bin(10) -> 0b1010
oct(10) -> 0o12
hex(10) -> 0xa
```

Remove prefix

```
oct(x)[2:]
hex(x)[2:]
bin(x)[2:]
```

---

# Hexadecimal Uppercase

```
hex(x)[2:].upper()
```

---

# Alignment

Right align using

```
string.rjust(width)
```

Example

```
"5".rjust(3)
```

Output

```
  5
```

---

# Algorithm

1. Read integer `n`
2. Calculate binary width
3. Loop from `1 → n`
4. Convert number to:

   * Decimal
   * Octal
   * Hexadecimal
   * Binary
5. Print values using `rjust(width)`

---

# Python Implementation

```python
def print_formatted(number):

    width = len(bin(number)) - 2

    for i in range(1, number + 1):

        decimal = str(i)
        octal = oct(i)[2:]
        hexa = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(
            decimal.rjust(width),
            octal.rjust(width),
            hexa.rjust(width),
            binary.rjust(width)
        )
```

---

# Complexity

```
Time  : O(n)
Space : O(1)
```

---

# Trick to Remember

```
width = len(bin(n)) - 2
```

All formatting depends on this width.
