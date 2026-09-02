def mul(a,b):
    if b==1:
        return a
    else:
        return a + mul(a,b-1)

a=mul(3,4)
print(a)