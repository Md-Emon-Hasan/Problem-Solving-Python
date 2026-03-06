# 82. Dictionary Key Removal: Given a dictionary of items and their quantities, write a Python program to remove a specific item from the dictionary based on user input.

items = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

item_to_remove = input("Enter item to remove: ")

items.pop(item_to_remove, None)

print("Updated dictionary:", items)