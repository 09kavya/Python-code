"""
    Remove all zeros from a number.

    Example:

    102030
    → 123
"""
num = int(input("Enter number: "))

result = 0
place = 1

while num > 0:
    digit = num % 10

    if digit != 0:
        result = result + digit * place
        place = place * 10

    num = num // 10

print(result)