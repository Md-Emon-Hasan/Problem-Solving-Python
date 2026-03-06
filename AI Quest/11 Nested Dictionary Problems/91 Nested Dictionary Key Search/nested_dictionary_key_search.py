# 91. Nested Dictionary Key Search: Write a Python program that takes a key as input and searches for it in a nested dictionary. If found, print the corresponding value, otherwise, print “Key Not Found.”

students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

search_key = input("Enter key to search: ")

found = False

for student in students:
    if search_key in students[student]:
        print(students[student][search_key])
        found = True

if not found:
    print("Key Not Found")