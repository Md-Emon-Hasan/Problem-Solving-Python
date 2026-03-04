# 13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

year = int(input("Enter a year: "))

if year % 400 == 0:
    print("Leap Year")
elif year % 4 == 0 and year % 100 != 0:
    print("Leap Year")
else:
    print("Not a Leap Year")