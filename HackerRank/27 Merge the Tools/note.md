# HackerRank – Merge the Tools!

## Problem

Given a string **S** and an integer **k**, split the string into **n/k substrings** of length **k**.

For each substring:

```
remove duplicate characters
keep the original order
print the result
```

---

# Example

Input

```
S = AABCAAADA
k = 3
```

Split string

```
AAB
CAA
ADA
```

After removing duplicates

```
AB
CA
AD
```

Output

```
AB
CA
AD
```

---

# Key Idea

Split the string into chunks of size `k`.

```
range(0, len(S), k)
```

Example

```
S = AABCAAADA
k = 3
```

Chunks

```
S[0:3] = AAB
S[3:6] = CAA
S[6:9] = ADA
```

---

# Removing Duplicates

Use a **set** to track seen characters.

```
seen = set()
```

If character not seen:

```
add to result
add to set
```

---

# Algorithm

1. Read string `S`
2. Read integer `k`
3. Loop from `0 → len(S)` with step `k`
4. Extract substring `S[i:i+k]`
5. Remove duplicate characters while maintaining order
6. Print result

---

# Python Implementation

```python
def merge_the_tools(string, k):

    for i in range(0, len(string), k):

        part = string[i:i+k]

        seen = set()
        result = ""

        for ch in part:

            if ch not in seen:
                seen.add(ch)
                result += ch

        print(result)
```

---

# Complexity

```
Time  : O(n)
Space : O(k)
```

---

# Trick to Remember

```
range(0, len(S), k)
```

This splits the string into **equal chunks of size k**.
