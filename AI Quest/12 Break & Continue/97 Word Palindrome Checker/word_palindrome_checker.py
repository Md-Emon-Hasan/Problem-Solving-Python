# 97. Word Palindrome Checker: Write a Python program that takes a word as input and checks if it is a palindrome (reads the same forwards and backward). Use `continue` to skip checking the word if its length is less than 3 characters.

while True:
    word = input('Enter a palindrome word:... ')
    
    if len(word) < 3:
        print('Word is too short')
        continue
    
    if word == word[::-1]:
        print(f'{word} is Pelindrome word')
    else:
        print(f'{word} Not palinedrome word')