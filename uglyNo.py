"""
Ugly Number

An ugly number is a positive integer whose prime factors are only 2, 3, and 5.

Given an integer n, determine whether n is an ugly number.

To check this, repeatedly divide n by 2, 3, and 5 as long as it is completely 
divisible by them. After removing all possible factors:

If the remaining value is 1, then n is an ugly number. 
If the remaining value is greater than 1, then n has another prime factor and is not an ugly number. 
Any n <= 0 is not an ugly number.

Example 1:
Input: n = 6 
Output: true 
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1 
Output: true 
Explanation: 1 has no prime factors.

Example 3:
Input: n = 14 
Output: false 
Explanation: 14 is not ugly since it includes the prime factor 7.
"""

def isUgly(n: int) -> bool:
    if n <= 0:
        return False

    while n % 2 == 0:
        n //= 2
    while n % 3 == 0:
        n //= 3
    while n % 5 == 0:
        n //= 5

    return n == 1

ans = isUgly(14)
print(ans)