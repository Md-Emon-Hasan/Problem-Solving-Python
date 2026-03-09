# Number Guessing Game

## Problem

Write a Python program that generates a random number between **1 and 100** and lets the user guess it.

Requirements:

- Use `while` loop
- Use `break` when correct number is guessed
- Use `continue` to keep prompting the user

---

# Theory

Random numbers in Python can be generated using the `random` module.

Example:

```
random.randint(a,b)
```

This returns a random integer between `a` and `b`.

Loop control statements:

```
break → exit loop
continue → skip iteration
```

---

# Approach

1. Import random module
2. Generate random number
3. Start infinite loop
4. Take user guess
5. Compare guess with secret number
6. Print hints
7. Break when correct

---

# Python Implementation

```python
import random

secret = random.randint(1,100)

while True:
    guess = int(input())

    if guess < secret:
        print("Too Low")
        continue

    if guess > secret:
        print("Too High")
        continue

    print("Correct")
    break
```

---

# Key Idea

Game loop pattern:

```
while True:
    input
    check
    continue / break
```