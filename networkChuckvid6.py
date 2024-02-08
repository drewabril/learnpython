# https://www.youtube.com/watch?v=nD1REhS6e3Y

import time
import os

print("Hello, welcome to Drew's Coffee")

name= input("What is your name?\n")

if name == "Ben" or name == "Patricia" or name == "Loki":
    evil_status = input("Are you Evil, " + name + "?\n")
    gooddeeds = int(input("How many good deeds have you done today?\n"))
    if evil_status == "Yes" and gooddeeds < 4:
        print("You gotta go, Evil " + name + ". GET OUT!")
        time.sleep(11)
        exit()
    else: 
        print("Welcome " + name)
else:
    print("Hello, " + name + "! Thank you for coming in! \n\n\n")


os.system('pause')
exit()