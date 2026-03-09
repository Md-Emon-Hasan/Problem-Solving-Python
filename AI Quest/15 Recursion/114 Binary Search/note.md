# Recursive Binary Search

## Problem

Write a recursive Python function `binary_search` that searches a **sorted list**.

Return:

```
index → if found
-1 → if not found
```

---

# Theory

Binary search works only on **sorted arrays**.

Idea:

```
1. Find middle element
2. Compare target
3. Search left or right half
```

Time Complexity:

```
O(log n)
```

Much faster than linear search.

---

# Approach

1. Define recursive function
2. Check base case
3. Find middle index
4. Compare target
5. Search left or right

---

# Python Implementation

```python
def binary_search(arr,target,left,right):

    if left > right:
        return -1

    mid = (left+right)//2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr,target,left,mid-1)

    else:
        return binary_search(arr,target,mid+1,right)
```

---

# Key Idea

Divide and conquer pattern:

```
mid = (left+right)//2
```