""" 
Isomorphic Strings

Difficulty: Easy
Category: Arrays & Hashing

Given two strings s and t, determine whether they are isomorphic.

Two strings are isomorphic if every character in s can be replaced with a character in t to make both strings identical, while preserving the order of characters.

The mapping must follow these rules:

1. Each character in s must always map to the same character in t.
2. Two different characters in s cannot map to the same character in t.
3. A character can map to itself.

Return true if the strings are isomorphic; otherwise, return false.

Examples

Example 1:
Input: {"s":"egg","t":"add"}
Output: true
"""
def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    pairs = set(zip(s, t))
    unique_s = set(s)
    unique_t = set(t)

    if len(pairs) == len(unique_s) and len(pairs) == len(unique_t):
        return True

    return False

ans = isIsomorphic("egg","add")
print(ans)