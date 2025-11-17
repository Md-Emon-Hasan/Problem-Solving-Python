# 18. Quadratic Equation Solver: Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and prints the real roots (if they exist) or a message indicating the complex roots.

import math

# Take coefficients as input
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if a is not zero
if a == 0:
    print("Not a quadratic equation (a cannot be 0).")
else:
    # Calculate discriminant
    D = b**2 - 4*a*c

    if D > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(D)) / (2*a)
        root2 = (-b - math.sqrt(D)) / (2*a)
        print(f"Two real roots: {root1} and {root2}")
    elif D == 0:
        # One real root (double root)
        root = -b / (2*a)
        print(f"One real root: {root}")
    else:
        # Complex roots
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-D) / (2*a)
        print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
