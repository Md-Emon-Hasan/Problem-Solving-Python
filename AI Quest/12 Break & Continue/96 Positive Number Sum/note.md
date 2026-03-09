# Positive Number Sum

## Problem
Write a Python program that takes positive numbers as input until a **negative number** is entered.

Then calculate and print the **sum of all positive numbers**.

Use:

```
while loop
break
```

---

# Theory

A `while` loop can run indefinitely using:

```
while True
```

The `break` statement stops the loop immediately.

This pattern is commonly used for **sentinel-controlled loops**.

Sentinel value here:

```
negative number
```

---

# Approach

1. Initialize sum variable
2. Start infinite loop
3. Take number input
4. If number is negative → break loop
5. Otherwise add to sum
6. Print total sum

---

# Python Implementation

```python
total = 0

while True:
    num = int(input())

    if num < 0:
        break

    total += num

print(total)
```

---

# Key Idea

Sentinel loop pattern:

```
while True:
    input
    if stop_condition:
        break
```