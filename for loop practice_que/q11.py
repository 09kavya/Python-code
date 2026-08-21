#Print no. from 1 to n that are divisible by 3 and 5
n=int(input("Enter the no. = "))

for i in range(1,n+1):
    if i%3==0 and i%5==0:
        print(f"The no. are divisible by 3 and 5 are {i}")