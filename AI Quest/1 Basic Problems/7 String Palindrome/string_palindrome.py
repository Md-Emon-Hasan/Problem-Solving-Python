# 7. String Palindrome: Write a Python function to check if a given string is a palindrome or not.

def is_palindrome(s:str) -> bool:
    return s == s[::-1]

user_input = input("Enter a string to check if it's a palindrome: ")
if is_palindrome(user_input):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")