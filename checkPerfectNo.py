"""  
Check for Perfect Number
Easy
Arrays & Hashing
Module: ASSIGNMENT
Check for Perfect Number
You are given an integer n. You need to check if the number is a perfect number or not. Return true if it is a perfect number, otherwise, return false.

A perfect number is a number whose proper divisors (excluding the number itself) add up to the number itself.

Examples
Example 1
Input:

{"n": 6}
Output:

true
Explanation: Proper divisors of 6 are 1, 2, 3. 1 + 2 + 3 = 6.
"""

def isPerfectNumber(n):
    sum = 1
    for i in range(2,n//2+1):
        if n%i==0:
            sum = sum + i
    
    return sum==n

result = isPerfectNumber(6)
print(result)