"""  
You are given an integer n. You need to check whether it is an Armstrong number or not. Return true if it is an Armstrong number, otherwise return false.

An Armstrong number is a number which is equal to the sum of the digits of the number, raised to the power of the number of digits.

Examples
Example 1:

Input: n = 153

Output: true

Explanation: Number of digits : 3.

1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153.

Therefore, it is an Armstrong number.
"""

def isArmstrong(n):
    original = n
    count = len(str(n))
    total = 0
    while n > 0:
        last = n % 10
        total = total + last ** count
        n = n // 10
        
    return total == original

ans = isArmstrong(153)
print(ans)