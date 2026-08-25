#Find the sum of digits until the number becomes 0

num=int(input("Enter the  number = "))
sum=0
while num> 0:
    digit=num%10
    sum=sum+digit
    num=num//10

print("Sum of digits =", sum)