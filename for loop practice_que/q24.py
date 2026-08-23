#check whether the no. is strong no.

num = int(input("Enter a number: "))

original = num
sum = 0

for i in range(len(str(num))):
    digit = num % 10

    fact = 1

    for j in range(1, digit + 1):
        fact = fact * j

    sum = sum + fact
    num = num // 10

if sum == original:
    print("Strong number")
else:
    print("Not a Strong number")