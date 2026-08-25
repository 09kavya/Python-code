#Find the smallest digit in a no.

num=int(input("Enter the number = "))

smallest=9

while num>0 :
    digit=num%10
    if digit<smallest :
        smallest=digit

    num=num//10

print(f" the smallest no. is {smallest}")


