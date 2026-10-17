"""   
An arithmetic series is a sequence of numbers in which the difference between consecutive terms remains constant. This difference is called the common difference.
You are given three integers n, a, and d, where a represents the first term of the series, d represents the common difference, and n represents the total number of terms.
The arithmetic series is defined as:
a, a + d, a + 2d, a + 3d, ...
Calculate and return the sum of the first n terms of the arithmetic series.
Example 1
Input: n = 5, a = 1, d = 3
Output: 35
Explanation:
The first five terms are 1, 4, 7, 10, 13. Their sum is 1 + 4 + 7 + 10 + 13 = 35.
Example 2
Input: n = 3, a = 1, d = 2
Output: 9
Explanation:
The first three terms are 1, 3, 5. Their sum is 1 + 3 + 5 = 9.
Constraints
- -1 <= n <= 500
- 0 <= a, d <= 500
"""

def sumOfAP(n, a, d):
        total = 0
        for i in range(n):
            total += a + i * d
        return total

ans  = sumOfAP(5,1,3)
print(ans)