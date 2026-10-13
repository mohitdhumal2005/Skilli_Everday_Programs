""" 
You are given an integer n. Your task is to return the largest digit present in the number.

Examples:
Example 1:

Input:

{"n": 25}
Output:

5
"""
def returnLargestDigit(n):
    # Write your code here
    largest = 0
    while n > 0:
        digit = n % 10
        if digit > largest:
            largest = digit
        n = n // 10
        
    return largest

ans = returnLargestDigit(99)
print(ans)