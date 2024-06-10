from art import logo, vs
from game_data import data
import random
import os



def selected(choice):
    name = choice['name']
    description = choice['description']
    country = choice['country']
    return(f"{name}, a {description}, from {country}")

def logic(choice):
    followers = choice['follower_count']
    return followers

print(logo)
choice1 = random.choice(data)


should_continue = True
current_score = 0
while should_continue:
    
    choice2 = random.choice(data)
    new = print(f"Compare A: {selected(choice1)}")
    print(vs)
    print(f"Against B: {selected(choice2)}")
    answer = input("Who has more followers? Type 'A' or 'B':\n").lower()
    

    followers = logic(choice1)
    followers2 = logic(choice2)
    os.system('cls')
    print(logo)

    life = 1

    if life > 0:
        
        if answer == 'a':
            if followers > followers2:
                current_score += 1
                print(f"You're right, your current score is {current_score}")
            else:
                life = 0
                print(f"Sorry, you're wrong. Your final score is {current_score}")
                
        else:
            if followers2 > followers:
                current_score += 1 
                print(f"You're right, your current score is {current_score}")
            else:
                life = 0
                print(f"Sorry, you're wrong. Your final score is {current_score}")
    choice1 = choice2
        
                
    if life == 0:
        print('Gameover')
        should_continue = False
                
