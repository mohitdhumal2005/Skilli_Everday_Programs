""" 
You are given two integers n1 and n2. Your task is to find the Lowest Common Multiple (LCM) of the two given numbers. The LCM of two integers is the smallest positive integer that is divisible by both integers.

Examples
Example 1:
Input:
n1 = 4, n2 = 6
Output:
12
Explanation:
4 * 3 = 12, 6 * 2 = 12.
12 is the lowest integer that is divisible by both 4 and 6.

Example 2:
Input:
n1 = 3, n2 = 5
Output:
15
"""

def findLcm(n1,n2):
    i = max(n1,n2)
    while True:
        if i % n1 == 0 and i % n2 == 0:
            return i
        i = i + 1

result = findLcm(3,5)
print(result)