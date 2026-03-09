# 108. Math Operations: Write a Python function called `math_operations` that takes three numbers and a string representing an operation (‘add’, ‘subtract’, ‘multiply’, or ‘divide’). The function should return the result of the specified operation on the three numbers. Implement the math operations as nested functions.

def math_operations(a, b, c, operation):

    def add():
        return a + b + c

    def subtract():
        return a - b - c

    def multiply():
        return a * b * c

    def divide():
        return a / b / c

    if operation == "add":
        return add()

    elif operation == "subtract":
        return subtract()

    elif operation == "multiply":
        return multiply()

    elif operation == "divide":
        return divide()

    else:
        return "Invalid operation"


# Testing the function
print(math_operations(10, 5, 2, "add"))
print(math_operations(10, 5, 2, "subtract"))
print(math_operations(10, 5, 2, "multiply"))
print(math_operations(10, 5, 2, "divide"))