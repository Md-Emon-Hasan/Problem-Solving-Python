number = input("Enter a number: ")

a, b = 0, 1

for i in range(int(number)):
    print(a, end=" ")
    a,b = b, a+b