nested_list = [[1,2,3],[4,5,6],[7,8,9]]

flattened_list = []

for i in nested_list:
    for j in i:
        flattened_list.append(j)

print(nested_list)
print(flattened_list)