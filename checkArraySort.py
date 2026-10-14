"""  
Given an array arr of size n, the task is to check if the given array is sorted in ascending (increasing or non-decreasing) order. If the array is sorted, return True; otherwise, return False.

Examples:
Example 1:
Input:
n = 5
arr = [1, 2, 3, 4, 5]
Output:
True
"""
def isArraySorted(arr):
    if sorted(arr) == arr:
        return True
    else:
        return False

result = isArraySorted([3,2,5,3,9])
print(result)