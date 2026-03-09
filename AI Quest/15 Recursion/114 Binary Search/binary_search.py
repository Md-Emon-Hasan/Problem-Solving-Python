# 114. Binary Search: Write a recursive Python function called `binary_search` that takes a sorted list and a target value as input and returns the index of the target value in the list using binary search. If the target value is not in the list, return -1.

def binary_search(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)

    else:
        return binary_search(arr, target, mid + 1, right)


# Testing the function
numbers = [2, 5, 8, 12, 16, 23, 38]

print(binary_search(numbers, 16, 0, len(numbers)-1))
print(binary_search(numbers, 5, 0, len(numbers)-1))
print(binary_search(numbers, 10, 0, len(numbers)-1))