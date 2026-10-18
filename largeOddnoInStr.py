"""  
Largest Odd Number
Given a string s representing a non-negative integer, find the largest-valued odd number that can be obtained as a substring of s.
The returned number must be a string and must not contain leading zeros. If no odd number exists, return an empty string "".
A substring is a contiguous sequence of characters within a string.
Examples
Example 1:
Input: s = "5347"
Output: "5347"
Explanation: The entire number 5347 is odd.
Example 2:
Input: s = "214638"
Output: "21463"
Explanation: The largest odd number is 21463.
Example 3:
Input: s = "4206"
Output: ""
Explanation: There is no odd digit, so no odd-valued substring exists.
Constraints
# - (1 leq s.length leq 10^5)
# - s consists only of digits (0 - 9).
"""

def largeOddNo(n):
    while n>0:
        if n%2!=0:
            return n
        else:
            n = n//10
    return ""

# ans = largeOddNo(23456)
ans = largeOddNo(0)
print(ans)
