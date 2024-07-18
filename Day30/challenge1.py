
import pandas
alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabets.to_dict()


data = {row.letter:row.code for (index, row) in alphabets.iterrows()}


is_true = True

while is_true:
    message = input("Enter something\n").upper()
    try:
        new = [data[letter] for letter in message]
    except KeyError:
        print("Sorry, only letters in the alphabets")
    else:
        is_true = False
        print(new)


