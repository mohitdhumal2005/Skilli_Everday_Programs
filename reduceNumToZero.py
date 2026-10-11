"""
Given a non-negative integer num, return the number of steps required to reduce it to 0. In each step:

If num is even, divide it by 2.
If num is odd, subtract 1 from it. Continue applying these operations until num becomes 0.
Example
For num = 14:
14 → 7 → 6 → 3 → 2 → 1 → 0 Total steps = 6. input:- 14
output:- 6
"""

def numberOfSteps(n):
    count = 0
    while n!=0:
        count = count+1
        if n%2==0:  
            n = n//2
        else:
           n = n-1
    return count
    
n = int(input("Enter a Number: "))
result = numberOfSteps(n)
print(result)