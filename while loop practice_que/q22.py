#Find the GCD using the Euclidean algorithm.

a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
while b!=0:
    remainder=a%b
    a=b
    b=remainder

print("GCD =", a)