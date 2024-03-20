import random

# list of words to choose from
words_list = ["practice", "python", "camel", "baboon", "ghana"]

# number of words in list 
word_list_number = len(words_list)

# selecting of word
select_word = random.randint(0, word_list_number-1)

# selected word
selected_word = words_list[select_word]
print(selected_word)

# selected word length for check in loop
word_length = len(selected_word)

# Chosen word list 
word = []
# listing spaces with loops
for letter in selected_word:
    word += '_'
print(word)

# welcoming front
print('Welcome to Hangman')

end_of_game = False
# loop for continuous game till game over 
while not end_of_game:
    # asking user for letter guess to start the game
    guess = input("To start, Guess a letter:\n").lower()

    #loop check
    for position in range(word_length):
        letter = selected_word[position]
        if letter == guess :
            word[position] = letter
    print(word)

    if '_' not in word:
        end_of_game = True
        print("You Win")