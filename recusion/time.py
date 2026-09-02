import time

def fibonacci(x):
    if x==0 or x==1:
        return 1
    else:
        return fibonacci(x-1)+fibonacci(x-2)

start=time.time()
print(fibonacci(27))
print(time.time()-start)