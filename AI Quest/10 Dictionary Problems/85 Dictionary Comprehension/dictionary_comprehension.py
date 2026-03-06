# 85. Dictionary Comprehension: Given a list of integers, write a Python program to create a dictionary where the keys are the elements from the list, and the values are their squares.

numbers = [1,2,3,4,5,6]

numbers_square = {x:x**2 for x in numbers}

print(numbers_square)