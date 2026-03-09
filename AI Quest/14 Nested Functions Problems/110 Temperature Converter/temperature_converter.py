# 110. Temperature Converter: Write a Python function called `temperature_converter` that takes a temperature value and a string representing the scale (‘C’ for Celsius or ‘F’ for Fahrenheit) as input. The function should convert the temperature from one scale to the other using nested functions and return the converted value.

def temperature_converter(temp, scale):

    def c_to_f():
        return (temp * 9/5) + 32

    def f_to_c():
        return (temp - 32) * 5/9

    if scale == "C":
        return c_to_f()

    elif scale == "F":
        return f_to_c()

    else:
        return "Invalid scale"


# Testing the function
print(temperature_converter(25, "C"))
print(temperature_converter(86, "F"))
print(temperature_converter(0, "C"))