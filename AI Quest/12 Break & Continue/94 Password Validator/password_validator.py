# 94. Password Validator: Write a Python program that takes a password as input and checks if it meets the following criteria: at least 8 characters long, contains both uppercase and lowercase letters, and has at least one digit. If the password is valid, print “Password accepted.” If not, use `continue` to prompt the user to enter a valid password.

while True:
    password = input("Enter password: ")

    if len(password) < 8:
        print("Password too short")
        continue

    has_upper = False
    has_lower = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Password accepted")
        break
    else:
        print("Invalid password")
        continue