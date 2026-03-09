# 105. List Sum Calculator: Write a Python function called `list_sum` that takes a list of integers as input and returns the sum of all elements in the list. Test the function with different lists.

def list_sum(number):
    
    total = 0
    
    for i in number:
        total += i
        
    return total
        
print(list_sum([10,20,30]))