# 99. Number Guessing Game: Write a Python program that generates a random number between 1 and 100 and lets the user guess the number. Use a `while` loop, `break` when the correct number is guessed, and `continue` to keep prompting the user until they guess correctly.

import random

random_number = random.randint(1,100)

while True:
    your_number = int(input('Enter your number:... '))
    if your_number == random_number:
        print('Congratulations!')
        break
    
    if your_number > random_number:
        print('Your guessing too high')
    else:
        print('You are gueesing too low')
    