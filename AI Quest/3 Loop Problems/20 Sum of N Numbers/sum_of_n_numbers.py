# 20. Sum of N Numbers: Write a Python program using a for loop to calculate the sum of the first N natural numbers, where N is taken as input from the user.

n = int(input('enter your numbers:...'))

sum = 0

for i in range(1, n+1):
    sum += i
    
print(sum)