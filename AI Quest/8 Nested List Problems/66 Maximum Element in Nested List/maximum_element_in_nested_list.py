# 66. Maximum Element in Nested List: Write a Python program to find the maximum element in a nested list of integers.

nested_list = [[1,2],[3,4],[5,6]]

max_number = nested_list[0][0]

for sub_list in nested_list:
    for element in sub_list:
        if element > max_number:
            max_number = element

print(max_number)