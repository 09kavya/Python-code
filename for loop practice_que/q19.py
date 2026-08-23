#frequency of each element in a list

list=[]
n=int(input(" Enter the list = "))
for i in range(1,n+1):
    a=int(input("Enter the list element = "))
    list.append(a)

check=[]
count=0

for i in list:
    if i not in check:
        count +=1
        for j in list:
            if i == j:
                count +=1
        print(i, "=", count)
        check.append(i)
        