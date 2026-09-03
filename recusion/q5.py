"""
Count the number of digits using recursion

Input: 123456
Output: 6
"""

def digit(num):
    if num==0:
        return 0
    return 1+ digit(num//10)
print(digit(12345))
