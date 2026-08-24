# find the missing no. from a list containing no. from 1 to n

n = int(input("Enter n: "))

list1 = []

for i in range(n - 1):
    num = int(input("Enter number: "))
    list1.append(num)

for i in range(1, n + 1):
    if i not in list1:
        print("Missing number =", i)