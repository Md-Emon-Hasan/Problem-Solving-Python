# 38. List Filtering: Given a list of integers, write a Python program to create a new list that contains only the even numbers from the original list.

numbers = [1,2,3,4,5,6]

even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)

print(even)