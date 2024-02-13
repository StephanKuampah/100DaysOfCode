print("Welcome to treasure Island")
print("Your misson is to find the hidden treasure of one piece")
crossroad = input('You are at a cossroad, Which way do you want to go? Type "left" ot "right".\n').lower()


if crossroad == "left" :
    choice_2 = input('You are at a river, Do you want to "wait" or "swim"\n').lower()
    if choice_2 == "wait":
        choice_3 = input('You came across three doors, Which door do you want to open? "Red"or "Yellow" or "Blue"\n').lower()
        if choice_3 == "red":
            print("You became food for lions. Game Over !!!")
        elif choice_3 == "blue":
            print("You got swallowed by a python. Game Over !!!")
        else:
            print("Congratulations, You found the one piece treasure !!!")
    else:
        print(" You got eaten by a shark. Game Over !!!")
else:
    print("You enterred a biohazard zone. Game Over !!!")