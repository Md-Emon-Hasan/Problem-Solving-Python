# 104. Even or Odd Checker: Write a Python function called `even_or_odd` that takes an integer as input and returns “Even” if the number is even and “Odd” if the number is odd. Test the function with different numbers.

def even_or_odd(number):
    if number % 2 == 0:
        print('Even')
    else:
        print('Odd')

even_or_odd(10)
even_or_odd(9)