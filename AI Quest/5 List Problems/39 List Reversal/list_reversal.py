# 39. List Reversal: Write a Python program to reverse a given list without using any built-in functions.

numbers = [1,2,3,4,5,6]

reversed = []

i = len(numbers) - 1

while i >= 0:
    reversed.append(numbers[i])
    i -= 1
    
print(reversed)