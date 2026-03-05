# 35. List Average: Write a Python program to calculate the average of all elements in a given list of integers.

numbers = [10, 20, 30, 40]

total = 0

for num in numbers:
    total += num

average = total / len(numbers)

print("Average:", average)