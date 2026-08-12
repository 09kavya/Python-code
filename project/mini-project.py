
menu={ "Pizza": 40,
      "Pasta": 50,
      "Burger": 50,
      "Salad": 70,
      "Coffee": 80 }
# print(menu)
print("Welcome to our restraunt. Here's the menu : ")
print("Pizza: Rs40\n","Pasta: Rs50\n","Burger: Rs50\n","Salad: Rs70\n", "Coffee: Rs80")
item_1=input("Enter the name of item you want to order ")
total=0
if item_1 in menu:
    total+=menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Order item {item_1} is not available yet!")
item_2=input("Do you want to add another order ? (Yes/No) ")
if item_2=="Yes":
    item_3=input("Enter your second order ")
    if item_3 in menu:
        total+=menu[item_3]
        print(f"Item {item_3} has been added to order")
    else:
        print(f"Order item {item_3} is not available yet!")
print(f"The total amount of items is {total}")