# 62. List of Tuples Conversion: Given a nested list containing tuples of (x, y) coordinates, write a Python program to convert it into a list of x-coordinates and a list of y-coordinates.

tuples_list = [(1,2),(3,4),(5,6)]

x_list = []
y_list = []

for x,y in tuples_list:
    x_list.append(x)
    y_list.append(y)
    
print(tuples_list)
print(x_list)
print(y_list)