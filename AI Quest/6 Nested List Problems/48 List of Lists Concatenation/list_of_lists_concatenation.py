# 48. List of Lists Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.

nested_list = [[1, 2], [3, 4], [5, 6]]

flat_list = []

for sublist in nested_list:
    for item in sublist:
        flat_list.append(item)

print("Concatenated list:", flat_list)