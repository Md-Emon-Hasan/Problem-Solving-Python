n, m = map(int, input().split())

# Top pattern
for i in range(1, n, 2):
    print((i * ".|.").center(m, "-"))

# Middle
print("WELCOME".center(m, "-"))

# Bottom pattern
for i in range(n-2, -1, -2):
    print((i * ".|.").center(m, "-"))