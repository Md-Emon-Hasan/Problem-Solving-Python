# 77. Dictionary Manipulation: Given a dictionary with student names as keys and their corresponding scores as values, write a Python program to add a new student to the dictionary and update the score of an existing student.

students = {
    "Alice": 85,
    "Bob": 90
}

# add new student
students["Charlie"] = 88

# update existing student score
students["Alice"] = 92

print("Updated dictionary:", students)