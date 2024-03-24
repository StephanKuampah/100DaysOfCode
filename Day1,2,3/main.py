print("Welcome to my roller-coaster")
height = int(input("what is your height in cm\n"))
if height >= 120:
    print("You can ride the roller-coaster")
    age = int(input("what is your age?\n"))
    if age < 12:
        print("You will pay $5")
    elif age <= 18:
        print("You will pay $7")
    else:
        print("You will pay $12")
else:
    print("sorry, you have to grow taller to ride this roller-coaster")
