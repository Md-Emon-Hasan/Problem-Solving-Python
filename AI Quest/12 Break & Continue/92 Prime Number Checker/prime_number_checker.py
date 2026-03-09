# 92. Prime Number Checker: Write a Python program that takes a number as input and determines if it is a prime number or not. Use a `for` loop to check for factors. If a factor is found, `break` out of the loop.

num = int(input("Enter a number: "))

is_prime = True

for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break

if is_prime and num > 1:
    print("Prime Number")
else:
    print("Not a Prime Number")