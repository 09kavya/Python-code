"""
Print numbers from N to 1 using recursion

Input: 5
Output: 5 4 3 2 1

"""
def num(n):
    if n==0:
        return 0
    print(n)
    num(n-1)

a=num(5)
print(a)