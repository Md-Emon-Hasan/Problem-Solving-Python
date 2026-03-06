# 84. Dictionary Frequency Count: Write a Python program that takes a string as input and creates a dictionary containing each character as a key and its frequency as the value.

text = input("Enter a string: ")

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print("Character frequency:", freq)