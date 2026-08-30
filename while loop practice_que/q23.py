#Convert decimal → binary without bin().

num=int(input("Enter a number : "))

binary=0
place=1

while num>0:
    digit=num %2
    binary=binary+digit*place
    place=place*10

    num=num//2

print("Binary =", binary)