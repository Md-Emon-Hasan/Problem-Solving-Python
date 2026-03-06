# 78. Dictionary Keys and Values: Write a Python program that takes a dictionary as input and prints all the keys and values in separate lines.

students = {
    'emon':10,
    'hasan':12,
    'imon':14
}

for key in students.keys():
    print(key)
    
for value in students.values():
    print(value)