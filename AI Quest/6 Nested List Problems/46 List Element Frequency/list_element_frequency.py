# 46. List Element Frequency: Given a nested list containing lists of integers, write a Python program to count the frequency of each element in the entire nested list.

nested_list = [[1, 2, 3], [2, 3, 4], [1, 2]]

frequency = {}

for sublist in nested_list:
    for num in sublist:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

print("Element frequencies:")
for key, value in frequency.items():
    print(key, ":", value)