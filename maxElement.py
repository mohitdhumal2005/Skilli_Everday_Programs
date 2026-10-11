""" 
Maximum Element
Given a non-empty list of integers nums, find and return the maximum value in the list without using the built-in max() function.

Example 1:
Input: nums = [1, 5, 3, 9, 2]
Output: 9
"""

def findMax(nums):
    maxNum = nums[0]
    for i in nums:
        if i > maxNum:
            maxNum = i
    return maxNum

result = findMax([1,5,9,3])
print(result)