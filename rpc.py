# making a rock , PAPER , SCISSORS games

import random

options=["ROCK","PAPER","SCISSORS"]
x=random.choice(options)
choice=x
your_option=input("Choose Between ROCK,PAPER,SCISSORS ")
Upp=your_option.upper()

print(x)

if choice=="ROCK" and Upp=="PAPER":
    print(f"YOU WIN {Upp} beats {choice}")
elif choice=="PAPER" and Upp=="SCISSORS":
    print(f"YOU WIN {Upp} beats {choice}")
elif choice=="SCISSORS" and Upp=="ROCK":
    print(f"YOU WIN {Upp} beats {choice}")
elif choice=="ROCK" and Upp=="SCISSORS":
    print(f"YOU LOST {choice} beats {Upp}")
elif choice=="SCISSORS" and Upp=="PAPER":
    print(f"YOU LOST {choice} beats {Upp}")
elif choice=="PAPER" and Upp=="ROCK":
    print(f"YOU LOST {choice} beats {Upp}")
elif choice==Upp:
    print("DRAW")
else:
    print("Invalid")
# print(choice) # using this to see what random output is 