# 57. Tuple Membership Test: Write a Python program that takes an element as input and checks if it exists in a given tuple.

t = (10, 20, 30, 40)

element = int(input("Enter element: "))

if element in t:
    print("Element exists in the tuple")
else:
    print("Element does not exist in the tuple")