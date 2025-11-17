# 19. Number Ranges: Write a Python program that takes an integer as input and prints whether the number falls within the ranges: 0-50, 51-100, 101-150, or above 150.

# Take integer input
num = int(input("Enter an integer: "))

# Check the range
if 0 <= num <= 50:
    print(f"{num} is in the range 0-50.")
elif 51 <= num <= 100:
    print(f"{num} is in the range 51-100.")
elif 101 <= num <= 150:
    print(f"{num} is in the range 101-150.")
elif num > 150:
    print(f"{num} is above 150.")
else:
    print(f"{num} is below 0.")
