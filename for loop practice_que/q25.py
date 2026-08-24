#gcd and lcm
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

for i in range(max(a, b), a * b + 1):
    if i % a == 0 and i % b == 0:
        lcm = i
        break

print("LCM =", lcm)