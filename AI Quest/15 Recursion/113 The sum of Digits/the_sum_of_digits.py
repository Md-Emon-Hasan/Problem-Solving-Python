# 113. The sum of Digits: Write a recursive Python function called `sum_of_digits` that takes an integer as input and returns the sum of its digits.

def Fibonacci(n):

    if n == 0:
        return 0

    if n == 1:
        return 1

    return Fibonacci(n - 1) + Fibonacci(n - 2)


# Testing the function
print(Fibonacci(5))
print(Fibonacci(7))
print(Fibonacci(10))