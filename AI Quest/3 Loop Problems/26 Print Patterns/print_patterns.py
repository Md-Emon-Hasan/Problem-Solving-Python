N = int(input("Enter the number of rows: "))

for i in range(1, N+1):
    for j in range(i):
        print("*", end="")
    print()


N = int(input("Enter the number of rows: "))

for i in range(N, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


N = int(input("Enter the number of rows: "))

for i in range(1, N+1):
    # print spaces
    for j in range(N - i):
        print(" ", end="")
    # print stars
    for k in range(2*i - 1):
        print("*", end="")
    print()


N = int(input("Enter the number of rows: "))

for i in range(N, 0, -1):
    # print spaces
    for j in range(N - i):
        print(" ", end="")
    # print stars
    for k in range(2*i - 1):
        print("*", end="")
    print()
