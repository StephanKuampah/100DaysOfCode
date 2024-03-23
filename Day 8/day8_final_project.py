def caesar(direction,text, shift):
    continue_cipher = True
    cipher_text = ""
    if direction == "decode":
        shift *= -1   
    for char in text:
        shift %= 26
        if (char in alphabet and direction != "decode" and direction != "encode"):
            continue_cipher = False
        elif char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += char
    if continue_cipher == True:
        print(f"The {direction}d text is, {cipher_text}")
    else:
        print("you have entered a wrong keyword")
        print("The keyword is 'encode' to encrypt and 'decode' to decrypt:\n") 
        
    
alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from caeser_cipher import logo
print(logo)
print("Welcome to caesar cipher")

should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction = direction, text = text, shift = shift)

    result = input("Type 'yes' try again or type 'no' to exit\n")
    if result == 'no':
        should_continue = False
        print('Goodbye, Come again.')