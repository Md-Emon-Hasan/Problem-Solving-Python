# 86. Dictionary Key Check: Write a Python program that takes a key as input and checks if it exists in a given dictionary. Print “Key Found” if the key is present and “Key Not Found” otherwise.

items = {
    "apple": 10,
    "banana": 5,
    "orange": 8
}

key = input("Enter key to search: ")

if key in items:
    print("Key Found")
else:
    print("Key Not Found")