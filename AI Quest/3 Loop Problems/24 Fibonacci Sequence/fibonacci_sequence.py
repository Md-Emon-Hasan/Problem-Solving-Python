# # 24. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.

N = int(input("Enter the limit N: "))

a, b = 0, 1

for i in range(N):
    print(a, end=" ")
    a,b = b , a+b
