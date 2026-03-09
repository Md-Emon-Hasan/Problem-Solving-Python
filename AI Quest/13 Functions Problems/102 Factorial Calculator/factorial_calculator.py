# 102. Factorial Calculator: Write a Python function called `factorial` that takes an integer as input and returns its factorial. Test the function with different values.

def number(n):
    
    sum = 1
    
    for i in range(1, n+1):
       sum *= i
    return sum

print(number(10))
print(number(9))