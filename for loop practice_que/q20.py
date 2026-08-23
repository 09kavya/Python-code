#check whether no. is armstrong no. or not

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

for i in range(digits):
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")