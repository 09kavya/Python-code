""""
    Print numbers from 1 to N using recursion

Input: 5
Output: 1 2 3 4 5

"""
def num(n):
    if n==0:
        return 0
    num(n-1)
    print(n)

print(num(5))