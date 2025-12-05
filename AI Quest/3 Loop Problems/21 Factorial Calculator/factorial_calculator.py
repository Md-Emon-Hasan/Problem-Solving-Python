# 21. Factorial Calculator: Write a Python program using a while loop to calculate the factorial of a given number N.

n = int(input('enter your numbers:...'))

factorial = 1

for i in range(1, n+1):
    factorial *= i
    
print(factorial)