# 45. Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a single-dimensional list.

nested_list = [[1,2],[3,4],[5,6]]

flattted_list = []

for list in nested_list:
    for i in list:
        flattted_list.append(i)
        
print(flattted_list)