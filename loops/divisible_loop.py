x=int(input("Enter 1st no. : "))
y=int(input("Enter 2nd no. : "))
z=int(input("Enter divisible no. : "))

y+=1

for i in range(x,y):
    if(i%z==0):
        print(i)
