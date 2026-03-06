# 52. Tuple Frequency Count: Given a tuple containing various elements, write a Python program to count the frequency of a specific element in the tuple.

my_tuple = (1,2,2,3,4,5,2)

target = 2
count = 0

for i in my_tuple:
    if i == target:
        count += 1

print(count)