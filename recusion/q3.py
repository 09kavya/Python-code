"""
Find the sum of first N natural numbers

Input: 5
Output: 15

"""
def sum(n):
    if n==0:
        return 0
    if n==1:
        return 1
    if n>1:
        return n+sum(n-1)


print(sum(5))
