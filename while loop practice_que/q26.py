#Keep taking input from the user until they enter 0, then print the sum of all entered numbers.

num=int(input())

sum=0

while num!=0:
    sum+=num
    num=int(input())
print(sum)