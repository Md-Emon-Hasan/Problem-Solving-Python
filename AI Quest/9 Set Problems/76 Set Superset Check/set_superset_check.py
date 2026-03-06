# 76. Set Superset Check: Given two sets A and B, write a Python program to check if set A is a superset of set B and print the result.

A = {1, 2, 3, 4}
B = {2, 3}

if A.issuperset(B):
    print("A is a superset of B")
else:
    print("A is not a superset of B")