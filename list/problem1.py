"""
define a function
take an input as how much big list you want
take list no
print sum of that no.

"""

def sum():
    lst=[]

    num=int(input("Enter the no. of list : "))

    for i in range(num):
        num1=int(input("Enter no.'s : "))
        lst.append(num1)

    total=0
    for i in range(len(lst)):
        total = total+lst[i]
    return f"Total is {total}"

s=sum()  
print(s) 