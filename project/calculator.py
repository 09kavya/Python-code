"""
Create a menu-driven calculator using while loop:
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit

"""

num1=int(input("Enter 1st number : "))
num2=int(input("Enter 2nd number : "))

while True:
    print("----------------ATM--------------")
    print("\n 1. Addition")
    print("\n 2. Subtraction")
    print("\n 3. Multiplication ")
    print("\n 4. Division")
    print("\n 5. Exit")
    print("---------------------------------")

    choice = int(input("Enter your choice: "))

    if choice==1:
        result=num1+num2
        print("After addition The result is ",result)

    elif choice==2:
        result=num1-num2
        print("After substraction The result is ",result)

    elif choice==3:
        result=num1*num2
        print("After multiplication The result is ",result)

    elif choice==4:
        result=num1/num2
        print("After division The result is ",result)

    elif choice==5:
        print("Thankyou for using calculator")
        break

    else:
        print("Invalid choice")


    

