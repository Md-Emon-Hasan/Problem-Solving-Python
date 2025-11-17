# 9. String Concatenation: Write a Python program that takes two strings as input and concatenates them into a single string without using the `+` operator.

str1 = input("enter first string:...")
str2 = input("enter second string...")

full_str = "".join([str1,str2])
print(full_str)