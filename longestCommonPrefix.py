"""  
Longest Common Prefix

Difficulty: Easy
Category: Arrays & Hashing

Given an array of strings str, find the longest common prefix shared by all the strings in the array.

A prefix is a sequence of characters that appears at the beginning of a string.

If there is no common prefix among all the strings, return an empty string "".

Example:

Example 1:-
Input: str = ["flowers", "flow", "fly", "flight"]
Output: "fl"
Explanation: All strings start with "fl", but their next characters are different. Therefore, the longest common prefix is "fl".

Example 2:-
Input: str = ["dog", "cat", "animal", "monkey"]
Output: ""
Explanation: No prefix is common to all the strings, so return an empty string.
"""
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""

    prefix = ""
    first = strs[0]

    for i in range(len(first)):
        ch = first[i]

        for word in strs:
            if i >= len(word) or word[i] != ch:
                return prefix

        prefix = prefix + ch

    return prefix

ans = longestCommonPrefix(["flower", "flow", "flight"])
print(ans)