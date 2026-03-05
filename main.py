number = [1,2,3,4,5]

sum = 0
maximum = number[0]
minimum = number[0]

for i in number:
    sum += i
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i
        
average = sum/len(number)

print("sum:... ", sum)
print("maximum:... ", maximum)
print("Minimum:... ", minimum)
print("Average:... ", average)