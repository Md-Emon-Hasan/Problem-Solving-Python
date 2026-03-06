# 56. Tuple Operations: Given two tuples of integers, write a Python program to perform element-wise addition, subtraction, and multiplication and create new tuples for each operation.

first_tuple = (5,6,7,8)
second_tuple = (1,2,3,4)

addition = ()
substraction = ()
multiplication = ()

for i in range(len(first_tuple)):
    addition += (first_tuple[i] + second_tuple[i],)
    substraction += (first_tuple[i] - second_tuple[i],)
    multiplication += (first_tuple[i] * second_tuple[i],)

print("Addition: ", addition)
print("Substraction: ", substraction)
print("Multiplication: ", multiplication)