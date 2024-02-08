#Let's start a coffee shop together. We're going to build a coffee shop using some new python programming concepts
# https://www.youtube.com/watch?v=T6OLDHAWjjA
# https://www.youtube.com/watch?v=5-5Mf_L0UKw

import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Hello, welcome to Drew's Coffee")

name= input("What is your name?\n")

if name == "Ben":
    evil_status = input("Are you Evil, Ben?\n")
    if evil_status == "Yes":
        print("You gotta go, Evil Ben. GET OUT!")
        exit()

print("Hello, " + name, " Thank you for coming in! \n\n\n")
menu = "Coffee, Espresso, Latte"

print(name + " , What would you like from our Menu today? Here is what we are serving. \n " + menu)


order = input("Type your order here: ")

if order == "Coffee":
    price = 3
elif order == "Espresso":
    price = 6
elif order == "Latte":
    price = 8
else:
    print("Sorry, we don't have that here.")
    exit()


print(name + ", can you confirm the total number of coffees you would like?")

orderquantity = input()



subtotal = price * int(orderquantity)

print("Ok, your total will be $" + str(subtotal))


print("Sounds good " + name + ", we'll have your " + orderquantity + " " + order + "s ready for you soon.")