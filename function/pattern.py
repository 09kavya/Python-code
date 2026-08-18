def lines():
    line=int(input("Enter the number of lines : "))
    for i in range(1,line+1):
        for j in range(i):
            print("*",end=" ")
        print( )

    return f"The {line} of no. triangle has been created"
triangle=lines()
print(triangle)
