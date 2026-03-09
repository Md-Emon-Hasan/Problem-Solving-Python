# 101. Unique Characters: Write a Python program that takes a string as input and checks if it contains all unique characters (no character repeats). Use a `for` loop and `break` when a character repeats.

text = input("Enter a string: ")

seen = set()
is_unique = True

for char in text:
    if char in seen:
        is_unique = False
        break
    seen.add(char)

if is_unique:
    print("All characters are unique")
else:
    print("Duplicate character found")