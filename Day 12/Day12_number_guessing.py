import random


numbers = [
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
    11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
    21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
    31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
    51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
    61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
    71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
    81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
    91, 92, 93, 94, 95, 96, 97, 98, 99, 100
]

chosen_number = random.choice(numbers)


print('Welcome to the number guessing game.')
difficulty = input("I am thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard':\n")
print(chosen_number)


attempts = ''
if difficulty == 'easy':
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess a number")
    should_continue = True
    while should_continue:
        answer =  int(input("Make a guess:\n"))
        if answer != chosen_number:
            attempts-= 1
            if attempts > 0:
                if answer > chosen_number:
                    print('Too High')
                else:
                    print('Too Low')
                print('Guess Again')
                print(f"You have {attempts} attempts remaining to guess a number")
            else:
                should_continue = False
                print('You lose')
        else:
            should_continue = False
            print(f"You got it! The answer is {answer}.")

else:
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess a number")
    should_continue = True
    while should_continue:
        answer =  int(input("Make a guess:\n"))
        if answer != chosen_number:
            attempts-= 1
            if attempts > 0:
                if answer > chosen_number:
                    print('Too High')
                else:
                    print('Too Low')
                print('Guess Again')
                print(f"You have {attempts} attempts remaining to guess a number")
            else:
                should_continue = False
                print('You lose')
        else:
            should_continue = False
            print(f"You got it! The answer is {answer}.")