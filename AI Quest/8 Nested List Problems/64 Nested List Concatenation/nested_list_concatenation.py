# 64. Nested List Concatenation: Given a list of nested lists, write a Python program to concatenate all the sublists into a single flat list.

nested_list = [[1,2],[3,4],[5,6]]

flat_list = []

for my_list in nested_list:
    for element in my_list:
        flat_list.append(element)
        
print(nested_list)
print(flat_list)