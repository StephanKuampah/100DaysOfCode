
import pandas
alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabets.to_dict()


data = {row.letter:row.code for (index, row) in alphabets.iterrows()}



message = input("Enter something\n").upper()

new = [data[letter] for letter in message]
print(new)