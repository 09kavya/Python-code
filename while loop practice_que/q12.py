#check the no. is palindrome or not
 
num=int(input("Enter the number = "))

original=num
rev=0

while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10

if original == rev:
    print("Palindrome  number")

else:
    print("Not a palindrome numeber")