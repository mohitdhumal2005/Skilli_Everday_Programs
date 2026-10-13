"""  
You are given two integers n1 and n2. Your task is to find the Greatest Common Divisor (GCD) of the two given numbers. The GCD of two integers is the largest positive integer that divides both of the integers without leaving a remainder.

Examples:
Example 1:
Input:

{"n1": 4, "n2": 6} 
Output:

2 
"""

def find_gcd(n1, n2):
    # Start with 1, because 1 divides every number
    gcd = 1

    # Find the smaller number
    if n1 < n2:
        smaller = n1
    else:
        smaller = n2

    # Check every number from 1 to the smaller number
    for i in range(1, smaller + 1):

        # If i divides both numbers, save it as the answer
        if n1 % i == 0:
            if n2 % i == 0:
                gcd = i

    return gcd


n1 = 4
n2 = 6

result = find_gcd(n1, n2)
print(result)