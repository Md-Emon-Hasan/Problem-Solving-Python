# 111. Factorial Calculation: Write a recursive Python function called `factorial` that takes a non-negative integer as input and returns its factorial.

def factorial(n):

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


# Testing the function
print(factorial(3))
print(factorial(5))
print(factorial(7))