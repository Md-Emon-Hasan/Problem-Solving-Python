# 7. String Palindrome: Write a Python function to check if a given string is a palindrome or not.

def palindrome(s:str)->bool:
    return s == s[::-1]
print(palindrome('mom'))
print(palindrome('cat'))
