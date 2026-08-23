#common elements between two lists whitout using set()

list=[]
n=int(input(" Enter the list = "))
for i in range(1,n+1):
    x=int(input("Enter the list element = "))
    list.append(x)

list1=[]
a=int(input(" Enter the list = "))
for i in range(1,a+1):
    y=int(input("Enter the list element = "))
    list1.append(y)

common=[]
for list2 in list:
    for list3 in list1:
        if  list2==list3 and list2 not in common:
            common.append(list2)
print("Common elements:", common)