#count how many prime number are present between 1 and n

n=int(input("Enter the number = "))

for i in range(1,n+1):
    if i <= 1:
        print(f"{i} Not Prime")
    else:
        for j in range(2, i):
            if i % j == 0:
                print(f"{i} Not Prime")
                break
        else:
            print(f"{i} Prime")