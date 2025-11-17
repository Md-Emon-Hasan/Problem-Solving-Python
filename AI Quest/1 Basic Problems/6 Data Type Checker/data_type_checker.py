# 6. Data Type Checker: Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).

def type_checker(data):
    return type(data)
print(type_checker(1))
print(type_checker(True))
print(type_checker('hello'))