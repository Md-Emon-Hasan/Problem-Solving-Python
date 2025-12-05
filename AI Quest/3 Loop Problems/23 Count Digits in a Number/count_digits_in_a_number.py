# 23. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.

# Take input from user
N = int(input("Enter a number: "))

num = abs(N)       # Negative number
count = 0

# Special case: if number is 0
if num == 0:
    count = 1
else:
    # Count digits using while loop
    while num > 0:
        num //= 10     # Remove last digit
        count += 1

print(f"Number of digits in {N} is: {count}")
