# Take input from user
N = int(input("Enter a number N: "))

sum_even = 0
i = 2  # even number 2

# Loop through all even numbers up to N
while i <= N:
    sum_even += i
    i += 2  # next even number

print(f"Sum of all even numbers between 1 and {N} is: {sum_even}")