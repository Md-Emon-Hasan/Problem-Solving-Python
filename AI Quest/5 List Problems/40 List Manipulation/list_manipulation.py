# 40. List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = []

for num in list1:
    if num in list2:
        common.append(num)

print("Common elements:", common)