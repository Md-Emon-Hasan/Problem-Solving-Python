# 88. Nested Dictionary Length: Write a Python program to calculate and print the total number of key-value pairs in a nested dictionary.

students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

total_pairs = 0

for student in students:
    total_pairs += len(students[student])

print("Total key-value pairs:", total_pairs)