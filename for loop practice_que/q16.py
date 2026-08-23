# find the second smallest no.in a list without sort( ) or max()

list=[]
n=int(input(" Enter the list = "))
for i in range(1,n+1):
    a=int(input("Enter the list element = "))
    list.append(a)

small=list[0]
second_small=list[0]

for num in list:
    if num<small:
        second_small=small
        small=num

    elif num<second_small and num != small:
        second_small=num

print(f"the second smallest number is {second_small}")