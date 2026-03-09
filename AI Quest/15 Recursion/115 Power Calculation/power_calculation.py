# 115. Power Calculation: Write a recursive Python function called `power` that takes two positive integers, base and exponent, as input and returns the value of base raised to the exponent.

def power(base, exponent):

    if exponent == 0:
        return 1

    return base * power(base, exponent - 1)


# Testing the function
print(power(2, 3))
print(power(3, 4))
print(power(5, 2))