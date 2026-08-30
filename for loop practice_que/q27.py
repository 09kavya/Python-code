# convert decimal no. into binary without bin()

num = int(input("Enter decimal number: "))

binary = 0
place = 1

for i in range(num):
    remainder = num % 2
    binary = remainder*place + binary 
    place=place * 10
    num = num // 2

print("Binary =", binary)