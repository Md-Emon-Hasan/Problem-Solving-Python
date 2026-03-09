# 100. Vowel Counter: Write a Python program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it. Use a `for` loop and `continue` to skip counting non-vowel characters.

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char not in vowels:
        continue
    count += 1

print("Number of vowels:", count)