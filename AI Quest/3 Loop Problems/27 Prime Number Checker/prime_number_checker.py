# 27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

# Take input from user
N = int(input("Enter a number: "))

is_prime = True

for i in range(2, N):
    if N % i == 0:
        is_prime = False
        break
    
if is_prime and N > 0:
    print(N, "Your number is prime")
else:
    print(N,'Number not prime')