"""
    Digit Sum and Product
Given a non-negative integer n, calculate the product of its digits and the sum of its digits, and return the difference: (product - sum).

Example 1:
Input: n = 234
Output: 15
Explanation: Product of digits = 2 * 3 * 4 = 24. Sum of digits = 2 + 3 + 4 = 9. Result = 24 - 9 = 15.
"""

def subtractProductAndSum(n):
    if n==0:
        print(n)
        return 
        
    sum = 0
    prod = 1
    while n>0:
        mod = n%10
        sum = sum + mod
        prod = prod * mod
        n = n//10
    print(prod-sum)

n = int(input("Enter Value for n: "))
subtractProductAndSum(n)