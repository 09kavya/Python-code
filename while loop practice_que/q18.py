#Count how many times a particular digit occurs.

num=int(input("Enter the number : "))
target=int(input("Enter the number : "))
count=0
while num>0:
    digit=num%10
    if digit==target:
        count+=1
    num=num//10

print("Digit occurs", count, "times")
