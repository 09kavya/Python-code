"""
Find the sum of digits of a number

Input: 12345
Output: 15
"""

def digit(n):
    
    if n==0:
        return 0
    return n%10 + digit(n//10)
print(digit(12345))

