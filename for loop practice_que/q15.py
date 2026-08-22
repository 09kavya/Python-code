# find the second lagest no.in a list without sort( ) or max()

list=[]
n=int(input(" Enter the list = "))
for i in range(1,n+1):
    a=int(input("Enter the list element = "))
    list.append(a)

print(list)

large=list[0]
second_large=list[0]

for num in list:
    if num > large:
        second_large=large
        large=num

    elif num>second_large and num!= large:
        second_large=num

print(f"the second largest number is {second_large}")


