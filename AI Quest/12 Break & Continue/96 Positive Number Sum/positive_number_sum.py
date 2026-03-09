# 96. Positive Number Sum: Write a Python program that takes positive numbers as input until a negative number is entered. Then, calculate and print the sum of all positive numbers entered. Use a `while` loop and `break` to exit the loop when a negative number is encountered.

sum_number = 0

while True:
    number = int(input('Enter Your Number:... '))
    if number < 0:
        break
    
    sum_number += number
    
print('Total sum:... ', sum_number)