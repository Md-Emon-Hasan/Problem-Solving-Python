# 112. Fibonacci Series: Write a recursive Python function called `Fibonacci` that takes an integer N as input and returns the Nth number in the Fibonacci series. The Fibonacci series is defined as follows: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1.

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