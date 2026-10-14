"""  
Given an array arr of n elements, the task is to reverse the given array in-place. The reversal should not create a new array; instead, it should modify the original array.

Examples
Example 1:

Input:

{"n": 5, "arr": [1, 2, 3, 4, 5]}
Output:

[5, 4, 3, 2, 1]
"""

def reverseArray(arr):
    return arr[::-1]

result = reverseArray([1,2,3,4])
print(result)