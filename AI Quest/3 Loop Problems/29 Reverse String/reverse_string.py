# 29. Reverse String: Write a Python program using a while loop to reverse a given string.

# Input string from user
s = input("Enter a string: ")

reversed_str = ""
i = len(s) - 1  # last index

# Loop from end to start
while i >= 0:
    reversed_str += s[i]
    i -= 1

print(f"Original string: {s}")
print(f"Reversed string: {reversed_str}")
