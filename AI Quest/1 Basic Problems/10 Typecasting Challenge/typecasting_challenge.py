# 10. Typecasting Challenge: Given three variables: `a = ‘100’`, `b = 25`, and `c = ‘10.5’`, write a Python program to perform the following operations and print the results: – Convert `a` to an integer and add it to `b`. – Convert `c` to a float and subtract it from the result of the first operation. – Convert the final result to a string and concatenate it with the string ” is the answer.”

# Given variables
a = '100'
b = 25
c = '10.5'

# Step 1: Convert `a` to integer and add to `b`
result1 = int(a) + b      # 100 + 25 = 125

# Step 2: Convert `c` to float and subtract from result1
result2 = result1 - float(c)  # 125 - 10.5 = 114.5

# Step 3: Convert final result to string and concatenate
final_result = str(result2) + " is the answer."

# Print the final result
print(final_result)
