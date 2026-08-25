#Find the largest digit in a no.

num=int(input("Enter the number = "))

largest=0

while num>0 :
    digit=num%10

    if digit>largest :
        largest=digit

    num=num//10

print(f"The largest number is {largest}")