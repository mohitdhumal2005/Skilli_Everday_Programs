def isPalindrome(n):
    return str(n) == str(n)[::-1]

result = isPalindrome(121)
print(result)