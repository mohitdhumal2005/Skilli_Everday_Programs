""" 
Swap Without Temporary Variable
Given two integers a and b, swap their values without using a third temporary variable. Return the swapped values as a list [a, b] (where the first element is the original b and the second element is the original a).

Example 1:
Input: a = 5, b = 10
Output: [10, 5]
"""
#Using Third variable
# a = 10
# b = 5
# c = a
# a = b
# b = c
# print(a)
# print(b)

def swapNumbers(a,b):
    a,b = b,a
    return([a,b])

result = swapNumbers(10,5)
print(result)


"""  Using Arithmetic Method:  """
# def swapNumbers1(a,b):
#     a = a+b
#     b = a-b
#     a = a-b
#     return([a,b])
# result = swapNumbers1(10,14)
# print(result)