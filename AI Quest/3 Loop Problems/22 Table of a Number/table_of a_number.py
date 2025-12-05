# 22. Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.

# Take input from users
n = int(input('enter your number:... '))

for i in range(1, 11):
    print(f'{i} x {n} = {i*n}')