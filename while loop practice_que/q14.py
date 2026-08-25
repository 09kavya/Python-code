#Count even and odd digits separately

num=int(input("Enter the number = " ))

count1=0
count2=0
a=0

while a<=num:

    if num%2==0:
        count1 +=1

    else:
        count2 +=1

    a += 1

print(f"The total even no. are {count1}")
print(f"The total odd no. are {count2}")
