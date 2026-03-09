# 98. Odd Number Finder: Write a Python program to find the first odd number from a list of integers. Use a `for` loop and `break` to stop the loop when the first odd number is found.

my_list = [2,4,5,6,7,8,9]

for item in my_list:
    if item % 2 != 0:
        print('Frist odd Number:...', item)
        break