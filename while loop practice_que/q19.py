#Check whether a number contains a particular digit.

num=int(input("Enter the number : "))
target=int(input("Enter the number : "))
count=False
while num>0:
    digit=num%10
    if digit==target:
        count=True
        break
    num=num//10

if count:
    print("Digit is present")
else:
    print("Digit is not present")