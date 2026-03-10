# HackerRank – Lists

## Problem

Perform list operations based on commands.

Commands:

```
insert i e
print
remove e
append e
sort
pop
reverse
```

---

# Theory

Python lists support multiple built-in operations:

```
append()
insert()
remove()
pop()
sort()
reverse()
```

---

# Approach

1. Create empty list
2. Read number of commands
3. For each command:
   - Parse command
   - Execute corresponding list operation

---

# Python Implementation

```python
N = int(input())
arr = []

for _ in range(N):
    command = input().split()

    if command[0] == "insert":
        arr.insert(int(command[1]), int(command[2]))

    elif command[0] == "print":
        print(arr)

    elif command[0] == "remove":
        arr.remove(int(command[1]))

    elif command[0] == "append":
        arr.append(int(command[1]))

    elif command[0] == "sort":
        arr.sort()

    elif command[0] == "pop":
        arr.pop()

    elif command[0] == "reverse":
        arr.reverse()
```

---

# Key Idea

Command parsing:

```
input().split()
```