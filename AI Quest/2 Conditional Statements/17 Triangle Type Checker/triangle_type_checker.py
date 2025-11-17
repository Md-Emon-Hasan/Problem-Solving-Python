# 17. Triangle Type Checker: Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, isosceles, or scalene triangle.

# Take three sides as input
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

# First, check if a valid triangle
if (a + b > c) and (a + c > b) and (b + c > a):
    # Determine triangle type
    if a == b == c:
        print("The triangle is Equilateral.")
    elif a == b or b == c or a == c:
        print("The triangle is Isosceles.")
    else:
        print("The triangle is Scalene.")
else:
    print("Not a valid triangle.")
