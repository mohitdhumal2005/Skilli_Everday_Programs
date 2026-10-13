""" 
You are given an integer n. Your task is to return the number of odd digits present in the number. The number will have no leading zeroes, except when the number is 0 itself.

Examples:
Example 1:

Input: n = 5

Output: 1

Explanation: 5 is an odd digit.

Example 2:

Input: n = 25
"""

def countOddDigits(n):
    # Write your code here
    count = 0
    while n > 0:
        if n % 2 == 1:
            count = count + 1
        n = n // 10

    return count
    pass

ans = countOddDigits(1234)
print(ans)