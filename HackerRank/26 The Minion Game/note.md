# HackerRank – The Minion Game

## Problem

Two players play a game with a string **S**.

Players:

```
Kevin
Stuart
```

Rules:

```
Kevin → substrings starting with vowels
Stuart → substrings starting with consonants
```

Vowels:

```
AEIOU
```

The player with the **highest score wins**.

---

# Example

Input

```
BANANA
```

Output

```
Stuart 12
```

---

# Key Insight

Instead of generating all substrings, use this trick:

If a substring starts at index `i`, the number of substrings possible is

```
n - i
```

Example

```
BANANA
length = 6
```

| index | character | substrings count |
| ----- | --------- | ---------------- |
| 0     | B         | 6                |
| 1     | A         | 5                |
| 2     | N         | 4                |
| 3     | A         | 3                |
| 4     | N         | 2                |
| 5     | A         | 1                |

---

# Score Calculation

If character is vowel

```
Kevin += n - i
```

Else

```
Stuart += n - i
```

---

# Algorithm

1. Read input string `S`
2. Initialize scores
3. Loop through each index
4. Check vowel or consonant
5. Add `n - i` to respective player
6. Compare scores and print winner

---

# Python Implementation

```python
def minion_game(string):

    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    for i in range(n):

        if string[i] in vowels:
            kevin_score += n - i
        else:
            stuart_score += n - i

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)

    elif stuart_score > kevin_score:
        print("Stuart", stuart_score)

    else:
        print("Draw")
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
substring count from index i = n - i
```

This avoids generating all substrings.
