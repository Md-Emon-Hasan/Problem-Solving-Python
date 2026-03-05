numbers = [12, 7, 25, 3, 18]

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
        
    if num < min_val:
        min_val = num

print("Maximum:", max_val)
print("Minimum:", min_val)