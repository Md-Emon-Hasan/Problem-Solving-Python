# 28. List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.

# Input list of integers
numbers = [10, 25, 7, 32, 18]

# Initialize variables
total = 0
maximum = numbers[0]
minimum = numbers[0]

# Loop through the list
for num in numbers:
    total += num
    if num > maximum:
        maximum = num
    if num < minimum:
        minimum = num

# Calculate average
average = total / len(numbers)

# Print results
print(f"List: {numbers}")
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")
