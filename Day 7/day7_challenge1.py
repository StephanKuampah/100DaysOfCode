import random


# import Hangman Stages
from hangman_art import stages,logo

# import word list
from hangman_words import words_list


# number of words in list 
word_list_number = len(words_list)

# selecting of word
select_word = random.randint(0, word_list_number-1)

# selected word
selected_word = words_list[select_word]


# selected word length for check in loop
word_length = len(selected_word)


# lives left
lives = 6

# Chosen word list 
word = []
# listing spaces with loops
for letter in selected_word:
    word += '_'
print(f'word\n')

# welcoming front
print(logo)
print('Welcome to Hangman\n')

end_of_game = False
# loop for continuous game till game over 
while not end_of_game:
    # asking user for letter guess to start the game
    guess = input("Guess a letter:\n").lower()

    # multiple word check 
    if guess in word:
        print("You already guessed {guess}")
    #loop check
    for position in range(word_length):
        letter = selected_word[position]
        if letter == guess :
            word[position] = letter
        
    if guess not in selected_word:
        lives -= 1
        print(f"{guess} is not in the word, you lose a life")
        if lives == 0:
            end_of_game = True
            print('')
            print(f'the word was {selected_word}\n')
            print("You got hanged.")
            print("You lose!!!")
            print("Gameover")
            
            
        else:
            print(stages[lives])
    print(f'{word}\n')

    if '_' not in word:
        end_of_game = True
        print("congratrulations")
        print("You Win")
print(stages[lives])



