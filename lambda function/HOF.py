#check the number is even odd or divisible by 3 and gives the sum of it

def return_sum(func,L):
    result=0
    for i in L:
        if func(i):
            result=result+i

    return result
list=[11,14,17,24,29,32,36,41]

x=lambda x: x%2==0
y=lambda x: x%2!=0
z=lambda x: x%3==0

print(return_sum(x,list))
print(return_sum(y,list))
print(return_sum(z,list))