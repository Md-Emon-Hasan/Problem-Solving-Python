# 15. Vowel or Consonant: Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.

char = input("enter a character:... ")

if char in 'aeiouAEIOU':
    print(char, 'is vowel')
else:
    print(char, 'is consonent')