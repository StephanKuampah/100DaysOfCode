import os
import random

from art import logo

# Function to clear the terminal screen
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# cards list
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# draw 2 cards function
def draw2():
    # start card 1 
    start_card1 = random.choice(cards)
    # start card 2
    start_card2 = random.choice(cards)
    return [start_card1, start_card2]

# draw 1 card function
def draw():
    return random.choice(cards)

# selected your start up cards
player_cards = draw2()

# computer cards
computer_cards = draw2()

# to start game
start_game = input("Do you want to play blackjack? 'yes' or 'no'\n")
should_continue = True

while should_continue:
    clear_terminal()
    if start_game.lower() == 'yes':
        print(logo)
        print(f"Your cards: {player_cards}")
        print(f"Computer's first card is {computer_cards[0]}")

        # Player's turn
        while sum(player_cards) < 21:
            to_continue = input("Do you want to draw another card? 'yes' to draw again or 'no' to get results\n")
            if to_continue.lower() == 'yes':
                new_card = draw()
                player_cards.append(new_card)
                print(f"Your cards: {player_cards}")
            elif to_continue.lower() == 'no':
                break

        # Computer's turn
        while sum(computer_cards) < 17:
            new_card = draw()
            computer_cards.append(new_card)

        
        # final cards
        print(f"Your final cards are {player_cards}")
        print(f"Computer's final cards are {computer_cards}")
        
        # Determine the winner
        if sum(player_cards) > 21:
            print("You lose")
        elif sum(player_cards) == 21:
            if sum(computer_cards) == 21:
                print("It's a draw")
            else:
                print("You win")
        elif sum(computer_cards) > 21:
            print("You win")
        elif sum(player_cards) > sum(computer_cards):
            print("You win")
        elif sum(player_cards) < sum(computer_cards):
            print("You lose")
        else:
            print("It's a draw")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? 'yes' or 'no'\n")
        if play_again.lower() != 'yes':
            should_continue = False
            print("Thank you for playing!")
    else:
        should_continue = False
        print("You did not start the game")
