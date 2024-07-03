# tODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
with open("B:/python study/Day 24_1/Input/Names/invited_names.txt") as file:
    name_file = file.readlines()



Names = []

for names in name_file:
    name = names.strip('\n')
    Names.append(name)

# # Replace the [name] placeholder with the actual name.
with open(".\Input\Letters\starting_letter.txt", mode="r") as file:
    content = file.read()

new_letters = []
for name in Names:
    content2 = content.replace("[name]", name)
    new_letters.append(content2)

paths = []
for name in Names:
    letter_path = f"B:\python study\Day 24_1\Output\ReadyToSend\letter_to_{name}.docx"
    paths.append(letter_path)



# #Save the letters in the folder "ReadyToSend".
for i in range(len(paths)):
    path = paths[i]
    content = new_letters[i]
    with open(path, mode="w") as write_file:
        write_file.write(content)


        
    





