"""Given a string, a character oldChar, and a character newChar, replace every occurrence of oldChar with newChar.

All other characters should remain unchanged.

Examples Example 1 Input: String = "banana" oldChar = 'a' newChar = 'x'

Output: "bxnxnx"

Example 2 Input: String = "hello" oldChar = 'l' newChar = 'p'

Output: "heppo"

Example 3 Input: String = "programming" oldChar = 'm' newChar = 'x'

Output: "prograxxing"

Output Format return the modified string."""

def replaceCharacter(s,oldChar,newChar):
    return s.replace(oldChar,newChar)
   


s = input("Enter a String: ")
print(s)
oldChar = input("Enter What you want to replace: ")
newChar = input("Enter the new Character: ")
result = replaceCharacter(s,oldChar,newChar)
print(result)