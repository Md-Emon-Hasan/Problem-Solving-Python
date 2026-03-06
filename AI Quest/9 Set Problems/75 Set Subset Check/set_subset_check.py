# 75. Set Subset Check: Given two sets A and B, write a Python program to check if set A is a subset of set B and print the result.

A = {1, 2}
B = {1, 2, 3, 4}

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")