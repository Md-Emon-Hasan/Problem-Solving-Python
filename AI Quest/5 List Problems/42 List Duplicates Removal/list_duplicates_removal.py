# 42. List Duplicates Removal: Write a Python program to remove duplicates from a given list while preserving the order of the elements.

numbers = [1, 2, 2, 3, 4, 3, 5]

result = []

for num in numbers:
    if num not in result:
        result.append(num)

print("List without duplicates:", result)