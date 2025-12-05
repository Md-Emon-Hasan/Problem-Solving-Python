# 27. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.

# Take input from user
N = int(input("Enter a number: "))

if N <= 1:
    print(f"{N} is not a prime number.")
else:
    i = 2
    is_prime = True
    
    while i * i <= N:  # check divisibility up to sqrt(N)
        if N % i == 0:
            is_prime = False
            break
        i += 1
    
    if is_prime:
        print(f"{N} is a prime number.")
    else:
        print(f"{N} is not a prime number.")
