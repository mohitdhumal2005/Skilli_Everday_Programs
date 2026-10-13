""" 
You are given an integer n. Your task is to return the integer formed by placing the digits of n in reverse order. Note that the result should not have leading zeros.

Examples
Example 1:

Input: n = 25

Output: 52

Explanation: The reverse of 25 is 52.
"""

def reverseInteger(n):
    # Write your code here
    return int(str(n)[::-1])

result = reverseInteger(-124)
print(result)

""" 
def reverseInteger(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_num = 0
    
    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10
        
    return reversed_num * sign
"""