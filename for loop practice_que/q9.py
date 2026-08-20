#write a program to calculate the factorial of a given no. such as 5

total=1
for n in range(5,0,-1):
    total *= n
    n-1

print(f"Total is {total}")