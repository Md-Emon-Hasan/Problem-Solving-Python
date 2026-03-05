# 25. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.

N = int(input("enter your number..."))

total = 0
n = 1

while n <= N:
    if n % 2 == 0:
        total += n
    n += 1
    
print(total)