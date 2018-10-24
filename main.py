# Originally developed by Manoj Tyagi
import random

def index():
    name = str(input("Enter your name ... "))
    print("Hello " + name)

    def thanks():
        print('Thanks for playing with me ... ')

    def roll():
        print("Let's roll the dice .... ")
        num = random.randint(1, 6)
        print("Hooray, you have got a number of " + str(num) + " on the dice...")
        choice = int(input('Do you want to roll the dice again ... (Type 1 for yes and 0 for No ) ... ?'))
        if choice == 0:
            thanks()
        elif choice == 1:
            roll()
        else:
            print('Invalid Choice ... ')
            thanks()

    roll()

index()
