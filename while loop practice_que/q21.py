#Keep reversing and adding a number until it becomes a palindrome.

num=int(input("Enter the number : "))

while True:
    temp=num
    reverse=0
    while temp>0:
        digit=temp%10
        reverse=reverse*10+digit
        temp=temp//10

    if num==reverse:
        break

    num=num+reverse

print("Palindrome =", num)   