# 54. Tuple Reversal: Write a Python program to reverse a tuple without using any built-in functions.

my_tuple = (1,2,3,4,5,6)

reverse_tuple = ()

i = len(my_tuple) - 1

while i >= 0:
    reverse_tuple += (my_tuple[i],)
    i -= 1
    
print(reverse_tuple)