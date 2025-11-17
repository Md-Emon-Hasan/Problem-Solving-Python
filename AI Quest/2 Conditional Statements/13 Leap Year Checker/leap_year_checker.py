# 13. Leap Year Checker: Write a Python program that takes a year as input and determines if it is a leap year or not.

year = int(input('Enter your year:... '))

if (year % 400 == 0):
    print(year, "is leap year")
elif (year % 100 == 0):
    print(year, "is not leap year")
elif (year % 4 ==0):
    print(year,  "is leap year")
else:
    print(year, "is leap year")