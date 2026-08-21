# calculate power of a number

num=int(input("Enter the base = "))
power=int(input("Enter the power = "))
i=1 
total=1 

while i<=power :
    total=num**i
    i+=1
print(total)
