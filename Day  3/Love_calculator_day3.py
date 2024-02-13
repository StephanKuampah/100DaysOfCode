print("Welcome to the Love Calculator")
Your_name = input("What is your name?\n")
Patners_name = input("What is your partner's name?\n")
Total_name = Your_name + Patners_name
Use_name = Total_name.lower()

t = Use_name.count("t")
r = Use_name.count("r")
u = Use_name.count("u")
e = Use_name.count("e")

true = str(t + r + u + e)

l = Use_name.count("l")
o = Use_name.count("o")
v = Use_name.count("v")
e = Use_name.count("e")

love = str(l + o + v + e)
calculated = int(true + love)


if (calculated < 10) or (calculated > 90 ):
    print(f"Your score is {calculated}, you go together like coke and menthos")
elif (calculated >= 40 ) and (calculated <= 50 ):
    print(f"Your score is {calculated}, you guys are alright together")
else:
    print(f"Your score is {calculated}")