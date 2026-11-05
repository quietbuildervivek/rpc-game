# making a rock , PAPER , SCISSORS games

import random

options=["ROCK","PAPER","SCISSORS"]
x=random.choice(options)
choice=x
your_option=int(input("Choose Between \n 1 for ROCK \n 2 for PAPER \n 3 for SCISSORS \n "))
if your_option==1:
    Upp="ROCK"
elif your_option==2:
    Upp="PAPER"
elif your_option==3:
    Upp="SCISSORS"
else:
    print("Invalid")

print("Computer chose: ",x)
print("You chose: ",Upp)

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