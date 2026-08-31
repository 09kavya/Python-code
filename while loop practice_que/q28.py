#decimal to hexadecimal

num= int(input("Enter the numer : "))
hexa="0123456789ABCDEF"
result=""

while num>0:
    digit=num%16
    result=result+hexa[digit]
    num=num//16

print(result)