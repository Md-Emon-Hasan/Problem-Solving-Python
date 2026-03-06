# 81. Dictionary Merging: Given two dictionaries, write a Python program to merge them into a single dictionary and print the result.

dict1 = {
    'a' : 1,
    'b' : 2
}

dict2 = {
    'c' : 3,
    'd' : 4
}

merged_dict = {**dict1, **dict2}

print(merged_dict)