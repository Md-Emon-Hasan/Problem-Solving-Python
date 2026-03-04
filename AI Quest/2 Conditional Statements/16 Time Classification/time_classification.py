# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

hour = int(input('enter your hour(0-23):.. '))

if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 16:
    print("Good Afternoon")
elif 17 <= hour <= 20:
    print("Good Evening")
else:
    print("Good Night")