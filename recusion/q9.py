"""
Find the sum of all even numbers from 1 to N

Input: 10
Output: 30

"""
def sum(num):
    if num==0:
        return 0
    
    return num + sum(num-2)
    

a=int(input("Enter a number :"))
print(sum(a))
    