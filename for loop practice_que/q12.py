#Find the sum of square s from 1 to n 

n=int(input("Enter the number = "))
square=1
total=0
for i in range(1,n+1):
    square= i*i
    total= total+square

print(f"the total is {total}")