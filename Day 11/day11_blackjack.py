import os
import random

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# cards list
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


# start card 1 
start_card1 = cards[random.choice(cards)]

# start card 2
start_card2 = cards[random.choice(cards)]

# selected start up cards
card = [start_card1,start_card2]

# printing 2 start up cards
print(card)

# function for drawing cards
# def draw():