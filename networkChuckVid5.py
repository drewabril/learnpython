import os

os.system('cls' if os.name == 'nt' else 'clear')

print("Hello, welcome to Drew's Coffee")

name= input("What is your name?\n")

if name == "Ben":
    evil_status = input("Are you Evil, Ben?\n")
    if evil_status == "Yes":
        print("You gotta go, Evil Ben. GET OUT!")
        exit()
    else: 
        print("Welcome Ben")

print("Hello, " + name, " Thank you for coming in! \n\n\n")

