import os
import random

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


# cards list
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]



def draw2():
    # start card 1 
    start_card1 = cards[random.choice(cards)]

    # start card 2
    start_card2 = cards[random.choice(cards)]
    
    return [start_card1,start_card2]

def draw():
    draw = cards[random.choice(cards)]
    return draw

# selected your start up cards
your_card = draw2()

# computer card
card = draw2()


# printing your start up cards
print(f"Your cards: {your_card}")
print(f"computer's first card is {card[0]}")
