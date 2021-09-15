print("Hi, Welcome to Naya's Burger PLace!")
print("Let's create an Account!")
print()
user = input("Enter a username: ").capitalize()
password = input("Enter a password: ")
print()
print("Registration Successful!")
print()
user_log = input("Login with your username: ")
user_pass = input("Password: ")

if user_log != user and user_pass != password:
    while user_log != user and user_pass != password:
        print()
        print("Incorrect Details! Try Again!")
        user_log = input("Login with your username: ")
        user_pass = input("Password: ")
else:
    print()
    print("Login Successful!")


print()
print("Hello, " + user + "! Welcome to Naya's Burger PLace!")
print("We have Burger with Fries which is $8, Just Burger which is $5, Fries is $5 and drink $2")
print()
print("For Burger and Fries, write B&F")
print("For Burger, write B")
print("For Fries, write F")
print("For Drink, write D")
order = input("What would you like?: ").upper()
tip = int(input("What would you like to leave as a tip?: $"))
if order == "B&F":
    quantity = int(input("How many would you like?: "))
    price = quantity * 8
    tax = price * 0.05
    total = tip + price + tax
    print()
    print("This is your bill...")
    print("Order: Burger and Fries")
    print("Quantity: ", quantity)
    print("Price: $", price)
    print("Tip: $", tip)
    print("Tax: $", tax)
    print("Total: $", total)
elif order == "B":
    quantity = int(input("How many would you like?: "))
    price = quantity * 5
    tax = price * 0.05
    total = tip + price + tax
    print()
    print("This is your bill...")
    print("Order: Burger")
    print("Quantity: ", quantity)
    print("Price: $", price)
    print("Tip: $", tip)
    print("Tax: $", tax)
    print("Total: $", total)
elif order == "F":
    quantity = int(input("How many would you like?: "))
    price = quantity * 5
    tax = price * 0.05
    total = tip + price + tax
    print()
    print("This is your bill...")
    print("Order: Fries")
    print("Quantity: ", quantity)
    print("Price: $", price)
    print("Tip: $", tip)
    print("Tax: $", tax)
    print("Total: $", total)
elif order == "D":
    quantity = int(input("How many would you like?: "))
    price = quantity * 2
    tax = price * 0.05
    total = tip + price + tax
    print()
    print("This is your bill...")
    print("Order: Drink")
    print("Quantity: ", quantity)
    print("Price: $", price)
    print("Tip: $", tip)
    print("Tax: $", tax)
    print("Total: $", total)
else:
    print("Invalid input!")
