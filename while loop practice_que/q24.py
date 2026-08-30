#Convert binary → decimal without int(binary, 2).


num=int(input("Enter a number : "))

decimal=0
place=1

while num>0:
    digit=num %10
    decimal=decimal+digit*place
    place=place*2

    num=num//10

print("Decimal =", decimal)