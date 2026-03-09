# 106. Greatest Common Divisor (GCD) Calculator: Write a Python function called `gcd` that takes two integers as input and returns their greatest common divisor. Test the function with different pairs of numbers.

def gcd(a,b):
    
    while b!= 0:
        a,b = b, a%b
    
    return a
    
print(gcd(12,18))