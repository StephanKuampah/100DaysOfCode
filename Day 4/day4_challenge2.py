import random
name_of_everyone = input("Give me everyone's name seperated with a comma\n")
names = name_of_everyone.split(",")
number_of_people = len(names)
result = random.randint(0,number_of_people-1)
name = names[result]
print(f"{name} is paying for the meal today!")