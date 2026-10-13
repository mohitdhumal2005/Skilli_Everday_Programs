""" 
You are given an integer n. Your task is to find out the number of prime numbers in the range [1, n] (inclusive). A prime number is defined as a number greater than 1 that has no divisors other than 1 and itself.

Examples
Example 1:

Input: n = 6
Output: 3
Explanation: The prime numbers in the range [1, 6] are 2, 3, 5.
Example 2:

Input: n = 10
Output: 4
Explanation: The prime numbers in the range [1, 10] are 2, 3, 5, 7.
"""
def countPrime(n):
    count = 0
    for i in range(2,n+1):
        prime = True
        for j in range(2,i):
            if i % j == 0:
                prime = False
                break
        
        if prime:
            count = count + 1
    return count

result = countPrime(6)
print(result)