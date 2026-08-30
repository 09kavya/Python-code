"""
Create a simple ATM menu using while loop:
1. Check Balance
2. Deposit
3. Withdraw
4. Exit

"""

balance=10000

while True:
    print("----------------ATM--------------")
    print("\n 1. Check Balance")
    print("\n 2. Deposite")
    print("\n 3. Withdraw ")
    print("\n 4. Exit")
    print("---------------------------------")

    choice = int(input("Enter your choice: "))

    if choice==1:
        print("Balance is",balance)

    elif choice==2:
        num=int(input("Enter deposite amount : "))
        balance=balance+num
        print("Amount deposited successfully")
        print("New Balance =", balance)

    elif choice==3:
        amount=int(input("Enter amount: "))

        if amount<=balance:
            balance=balance-amount
            print("Please collect your cash")
            print("Remaining Balance =", balance)

        else:
            print("Insufficient Balance")

    elif choice==4:
        print("Thank you for using ATM")
        break

    else:
        print("Invalid choice")


    

