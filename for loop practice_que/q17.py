#duplictae element in a list

list=[]
n=int(input(" Enter the list = "))
for i in range(1,n+1):
    a=int(input("Enter the list element = "))
    list.append(a)



duplicate=[]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j] and i  not in duplicate:
            duplicate.append(list[i])

print("Duplicate elements:", duplicate)  