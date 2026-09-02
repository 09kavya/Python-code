#if 2newborn rabbits are put in a pen , how many rabbits will be in the pen after 1  year

def fibonacci(x):
   
    if x<=1:
        return x
    
    return fibonacci(x-1)+fibonacci(x-2)


for i in range(12):
    print(fibonacci(i), end=" ")
