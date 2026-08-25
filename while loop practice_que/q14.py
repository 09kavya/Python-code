#Count even and odd digits separately

num = int(input("Enter the number = "))

even = 0
odd = 0

while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    num = num // 10

print("Even =", even)
print("Odd =", odd)