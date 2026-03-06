# 65. Count Even Numbers: Write a Python program to count the number of even numbers in a nested list.

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8]]

count = 0

for sublist in nested_list:
    for num in sublist:
        if num % 2 == 0:
            count += 1

print("Number of even numbers:", count)