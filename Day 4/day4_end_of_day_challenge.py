import random

choices = ["rock", "paper", "scissors"]
choice = len(choices)
outcomes = random.randint(0,choice-1)
outcome = choices[outcomes]
print("Welcome to my rock, paper, scissors game.\n")
start = input("What would you like to choose? '0' for rock '1' for paper '2' for scissors.\n")



if start == '0':
    print("you chose rock.")
    print(f"we choose {outcome}.")
    if outcome == choices[0] :
        print("Oh no, It's a tie")
    elif outcome == choices[1]:
        print("Hahaha, You lose")
    else:
        print("Congrats, You Win")
elif start == '1':
    print("you chose paper.")
    print(f"we choose {outcome}.")
    if outcome == choices[1] :
        print("Oh no, It's a tie")
    elif outcome == choices[2]:
        print("You lose")
    else:
        print("Congrats, You Win")
elif start == '2':
    print("you chose scissors.")
    print(f"we choose {outcome}.")
    if outcome == choices[2] :
        print("Oh no, It's a tie")
    elif outcome == choices[0]:
        print("Hahaha, You lose")
    else:
        print("Congrats, You Win")
else:
    print('You chose an invalid number, You lose')


start_again = input("do you want to play again?\n")




    
