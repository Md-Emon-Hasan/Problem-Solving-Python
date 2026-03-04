# Count Digits in a Number

## Problem
Write a Python program using a **while loop** to count the number of digits in a given integer **N**.

Example

Input
```
12345
```

Output
```
5
```

---

# Theory

Each digit of a number can be removed using **integer division by 10**.

Example:

```
1234 // 10 = 123
123 // 10 = 12
12 // 10 = 1
1 // 10 = 0
```

Each division removes the **last digit**.

By counting how many times this operation occurs, we can determine the **number of digits**.

---

# Approach

1. Take integer input `N`
2. Initialize `count = 0`
3. Use a `while` loop while `N != 0`
4. Remove the last digit using `N //= 10`
5. Increase `count`
6. Print the count

---

# Python Implementation

```python
N = int(input())

count = 0

while N != 0:
    N //= 10
    count += 1

print(count)
```

---

# Key Idea

Remove digits using:

```
N //= 10
```

and count iterations.