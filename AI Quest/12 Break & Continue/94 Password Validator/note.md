# Password Validator

## Problem

Write a Python program that validates a password with the following rules:

- Minimum length = 8
- Must contain uppercase letters
- Must contain lowercase letters
- Must contain at least one digit

If password is valid:

```
Password accepted
```

Otherwise ask again using `continue`.

---

# Theory

Password validation checks multiple conditions.

Useful Python string methods:

```
isupper()
islower()
isdigit()
```

These methods help identify character types.

---

# Approach

1. Use infinite loop (`while True`)
2. Take password input
3. Check length
4. Traverse characters
5. Detect uppercase, lowercase, digit
6. If valid → break loop
7. Otherwise continue

---

# Python Implementation

```python
while True:
    password = input()

    if len(password) < 8:
        continue

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Password accepted")
        break
```

---

# Key Idea

Password validation pattern:

```
while True:
    check conditions
    if valid:
        break
    else:
        continue
```