""" 
Given an array arr of size n, your task is to find the sum of all the elements in the array.

Examples
Example 1: Input:

{"n": 5, "arr": [1, 2, 3, 4, 5]}
Output:

15
"""
def sumOfArrayElements(n,arr):
    sum = 0
    for i in arr:
        sum = sum+i
    return sum

result = sumOfArrayElements(5,[1,2,3,4,5])
print(result)