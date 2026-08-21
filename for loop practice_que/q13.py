#find the sum of cubes from 1 to n


n=int(input("Enter the number = "))
cube=1
total=0
for i in range(1,n+1):
    cube=i**3
    total= total+ cube

print(total)