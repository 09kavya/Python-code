"""
    [1,2,3,4,5]
    [1,2,6,7,8]

    common[1,2]

"""
def common():
    lst=[]
    lst_1=[]
    num=int(input("Enter the no. first of list : "))
    
    for i in range(num):
        num1=int(input("Enter no.'s : "))
        lst.append(num1)
    # print(lst)

    num1=int(input("Enter the no. second of list : "))
    for j in range(num1):
        num2=int(input("Enter no.'s : "))
        lst_1.append(num2)
    # print(lst_1)

    a=set(lst)
    b=set(lst_1)
    unique=a.intersection(b)
    print(unique)

common()