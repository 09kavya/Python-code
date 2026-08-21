#check wheather the no. is perfect square or not

num=int(input("Ente a number to check= "))
i=1
is_perfect_square=False

while i*i<=num:
    if i*i == num:
        is_perfect_square=True
        break
    i+=1

if is_perfect_square:
    print(f"{num} is a perfect square")

else:
    print(f"{num} is not a perfect square")