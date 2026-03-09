# 109. Greeting Generator: Write a Python function called `greeting_generator` that takes a name as input and returns a greeting message using nested functions. The greeting message should be customizable (e.g., “Hello, {name}! How are you today?”).

def greeting_generator(name):

    def create_greeting():
        return f"Hello, {name}! How are you today?"

    return create_greeting()


# Testing the function
print(greeting_generator("Emon"))
print(greeting_generator("Alice"))
print(greeting_generator("Bob"))