# 83. Dictionary Sorting: Given a dictionary with names as keys and corresponding ages as values, write a Python program to sort the dictionary based on age in ascending order.

people = {
    "Alice": 25,
    "Bob": 20,
    "Charlie": 30
}

sorted_people = dict(sorted(people.items(), key=lambda x: x[1]))

print("Sorted dictionary:", sorted_people)