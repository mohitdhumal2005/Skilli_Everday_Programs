"""  
You are given an integer n. Return the value of n! (n factorial). The factorial of a number is the product of all positive integers less than or equal to that number.

Examples
Example 1:

Input:

{"n": 2}
Output:

2
Explanation: 2! = 1 * 2 = 2.
"""
def factorial(n):
    
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i

    return fact

ans = factorial(3)
print(ans)