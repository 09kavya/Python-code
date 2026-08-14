"""
 [1,2,3,4,5]

 return max and min value   

"""
def value():
    lst=[]
    num=int(input("Enter the no. of list : "))
    
    for i in range(num):
        num1=int(input("Enter no.'s : "))
        lst.append(num1)

    print(lst)
    maximum=max(lst)
    print(f"The maximum number of list is {maximum}")
    minimum=min(lst)
    print(f"The minimum number of list is {minimum}")

value()