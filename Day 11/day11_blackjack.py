import os
import random
from art import logo

# Function to clear the terminal screen
def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Function to draw 2 cards
def draw2():
    start_card1 = random.choice(cards)
    start_card2 = random.choice(cards)
    return [start_card1, start_card2]

# Function to draw 1 card
def draw():
    return random.choice(cards)

# List of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def ace_check():
    # If sum of cards is greater than 21 and there's an ace (11), consider it as 1
        if sum(cards) > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
        return sum(cards)


should_continue = True
while should_continue:
    # welcome
    print("Welcome to blackjack")
    
    # Start the game
    start_game = input("Do you want to play blackjack? 'yes' or 'no'\n")
    
    if start_game.lower() == 'yes':
        clear_terminal() 
        player_cards = draw2()
        computer_cards = draw2()
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
        while sum(computer_cards) < 17 and sum(player_cards) <= 21:
            new_card = draw()
            computer_cards.append(new_card)    

        ace_check() 


        # Final cards
        print(f"Your final cards are {player_cards}")
        print(f"Computer's final cards are {computer_cards}")

        # Determine the winner
        player_score = sum(player_cards)
        computer_score = sum(computer_cards)
        if player_score > 21:
            print("You lose")
        elif player_score == 21:
            if computer_score == 21:
                print("It's a draw")
            else:
                print("You win")
        elif computer_score > 21:
            print("You win")
        elif player_score > computer_score and player_score <= 21 and computer_score <= 21:
            print("You win")
        elif player_score < computer_score and player_score <= 21 and computer_score <= 21:
            print("You lose")
        else:
            print("It's a draw")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? 'yes' or 'no'\n")
        if play_again == 'yes':
            clear_terminal()
        else:
            print('Thank You for playing')
       
    else:
        should_continue = False
        print("You did not start the game")
