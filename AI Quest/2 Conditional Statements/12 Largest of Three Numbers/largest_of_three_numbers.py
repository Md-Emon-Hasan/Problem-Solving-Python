# 12. Largest of Three Numbers: Write a Python program that takes three numbers as input and prints the largest among them.

first_number = float(input('enter your first number:... '))
second_number = float(input('enter your second number:... '))
third_number = float(input('enter your third number:... '))

if first_number >= second_number and first_number >= third_number:
    print("Largest number is:... ", first_number)
elif second_number >= third_number and second_number >= first_number:
    print('Largest number is:... ', second_number)
else:
    print('Largest number is:...', third_number)