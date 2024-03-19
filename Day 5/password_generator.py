import random
# Password characters
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['%','#','!','$','&',')','(','*','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']

# Input area
print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters do you want in your password?\n"))
number_numbers = int(input("How many numbers do you want in your password?\n"))
number_symbols = int(input("How many symbols do you want in your password?\n"))

#genrator
password = []
for letter in range (1,number_letters + 1):
    result = random.choice(letters)
    password += result
    # print(result)

for number in range (1,number_numbers + 1):
    result2 = random.choice(numbers)
    password += result2
    # print(result2)

for symbol in range (1,number_symbols + 1):
    result3 = random.choice(symbols)
    password += result3
    # print(result3)

#shuffling password
random.shuffle(password)

final_password = ""
for passwords in password:
    final_password += passwords

#final output
print(f'Your password is \n{final_password}')
