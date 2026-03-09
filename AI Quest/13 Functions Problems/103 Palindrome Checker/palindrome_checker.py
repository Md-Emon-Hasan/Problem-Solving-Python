# 103. Palindrome Checker: Write a Python function called `is_palindrome` that takes a string as input and returns `True` if it is a palindrome and `False` otherwise. Test the function with different words.

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

print(is_palindrome('hello'))
print(is_palindrome('wow'))