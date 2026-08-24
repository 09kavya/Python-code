# convert decimal no. into binary without bin()

num = int(input("Enter decimal number: "))

binary = ""

for i in range(num):
    remainder = num % 2
    binary = str(remainder) + binary
    num = num // 2

print("Binary =", binary)