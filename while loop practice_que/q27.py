#decimal to octal
num=int(input("Enter number : "))
octal=0
place=1
while (num>0):
    digit=num%8
    octal=octal + digit*place
    place=place*10
    num=num//8

print(octal)