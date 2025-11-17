# 5. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user

# Take input from user
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)

fahrenheit = float(input("Enter tempreture in Fahrenheit: "))
celcius = (fahrenheit - 32) * 5/9

print(celcius)
