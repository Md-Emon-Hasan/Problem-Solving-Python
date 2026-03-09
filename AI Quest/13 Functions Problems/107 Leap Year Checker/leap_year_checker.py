# 107. Leap Year Checker: Write a Python function called `is_leap_year` that takes a year as input and returns `True` if it is a leap year and `False` otherwise. Test the function with different years.

def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Testing the function
print(is_leap_year(2020))
print(is_leap_year(2023))
print(is_leap_year(2000))
print(is_leap_year(1900))