# 43. List Comprehension: Given a list of integers, write a Python program to create a new list that contains the squares of the elements using list comprehension.

numbers = [1,2,3,4,5,6,7,8,9]

square = [number**2 for number in numbers]

print(square)