""" 
Given an array of n elements, the task is to return the count of the number of odd numbers in the array.

Examples
Example 1:

Input: n=5, array = [1,2,3,4,5]
Output: 3
Explanation: The three odd elements are (1, 3, 5)
"""

def countOddNos(n,arr):
    count = 0
    for i in arr:
        if i%2!=0:
            count = count + 1
    return count

result = countOddNos(5,[1,2,3,4,5])
print(result)