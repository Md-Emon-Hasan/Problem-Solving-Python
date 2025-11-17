# 16. Time Classification: Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, “Good Evening”, or “Good Night” based on the time.

hour = int(input('enter your hour(0-23):.. '))

if hour <= 12:
    print('Good Moorning')
elif hour >= 12 and hour < 17:
    print('Good Aftrenoon')
elif hour >= 17 and hour < 21:
    print('Good Evening')
else:
    print('Good Night')