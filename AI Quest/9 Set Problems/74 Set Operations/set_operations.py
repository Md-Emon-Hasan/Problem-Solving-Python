# 74. Set Operations: Given three sets A, B, and C, write a Python program to find and print the intersection of A and B, the union of B and C, and the difference between C and A.

A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

intersection_result = A & B
union_result = B | C
difference_result = C - A

print("Intersection of A and B:", intersection_result)
print("Union of B and C:", union_result)
print("Difference of C and A:", difference_result)