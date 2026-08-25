#reverse a no using without converting it to a string

num = int(input("Enter the number = "))

rev = 0

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

print("Reverse =", rev)