# 41. List Element Count: Write a Python program to count the occurrences of a specific element in a given list.

numbers = [1,2,3,4,2,5,6,2]

target = 2
count = 0

for i in numbers:
    if target == i:
        count += 1
        
print(count)