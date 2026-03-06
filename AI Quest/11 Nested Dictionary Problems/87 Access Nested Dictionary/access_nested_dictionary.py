# 87. Access Nested Dictionary: Given a nested dictionary containing student details, write a Python program to access and print specific information such as a student’s name, age, and address.

students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "address": "New York"
    }
}

name = students["student1"]["name"]
age = students["student1"]["age"]
address = students["student1"]["address"]

print("Name:", name)
print("Age:", age)
print("Address:", address)