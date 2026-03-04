# String Concatenation Without Using `+`

## Problem
Write a Python program that takes two strings as input and concatenates them into a single string **without using the `+` operator**.

Example

Input
```
Hello
World
```

Output
```
HelloWorld
```

---

# Theory

String concatenation means **joining two or more strings together**.

Normally we use the `+` operator:

```
"Hello" + "World"
```

But Python also provides the **`join()` method**, which is often more efficient when combining multiple strings.

Syntax

```
separator.join(iterable)
```

Where:

- `separator` is placed between elements
- `iterable` is a list or tuple of strings

If we use an empty string as the separator:

```
"".join([...])
```

then the strings are joined directly.

---

# Approach

1. Take two strings as input
2. Put them into a list
3. Use `join()` to combine them
4. Print the result

---

# Python Implementation

```python
str1 = input()
str2 = input()

result = "".join([str1, str2])

print(result)
```

---

# Key Idea

Use the `join()` method:

```
"".join([str1, str2])
```

to concatenate strings **without using `+`**.