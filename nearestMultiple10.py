"""   
You are given a string representing a positive integer. Your task is to round the number to the nearest multiple of 10. If the number is equally distant from two multiples of 10, return the smaller multiple. Return the rounded number as a string.

Example 1:

Input: s = "29"

Output: "30"

Explanation: The nearest multiples of 10 are 20 and 30. Since 29 is closer to 30, the answer is 30.

Example 2:

Input: s = "15"

Output: "10"

Explanation: The number 15 is equally distant from 10 and 20. Since we choose the smaller multiple in a tie, the answer is 10.

Constraints:

\- 1
"""

def roundTonearest(s):
    lower = (s//10)*10
    upper = lower + 10
    
    
    if s-lower < upper-s:
        return lower
    elif s-lower > upper-s:
        return upper
    else:
        return lower


ans = roundTonearest(29)
print(ans)
    