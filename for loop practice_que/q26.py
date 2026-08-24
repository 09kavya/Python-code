#hcf

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

HCF = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        HCF = i

print("HCF =", HCF)