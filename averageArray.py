"""  
Given an integer array arr of size n, calculate the mean (average) of all the elements in the array and return its floor value.

The mean is calculated by dividing the sum of all array elements by the total number of elements.

The floor value is the greatest integer less than or equal to the calculated mean.

Examples:
Example 1:-
Input: arr = [1, 3, 4, 2, 6, 5, 8, 7]
Output: 4
"""

def avgArray(arr):
    sum = 0
    lenArr = len(arr)
    for i in arr:
        sum = sum + i
    avg = sum//lenArr
    return avg

ans = avgArray([1,2,3,4,5,6,7])
print(ans)