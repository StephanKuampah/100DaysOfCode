MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def pay():
    total = 0
    print("Please insert coins.")
    total += int(input("How many quarters?: ")) * 0.25 
    total+= int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickels?: "))* 0.05 
    total += int(input("How many pennies?: ")) * 0.01
    return total

def change(cost, paid):
    if paid >= cost:
        change = round(paid - cost,2)
        global money
        money += change
        print(f"Here is ${change} in change")
        return True  
    else:
        print("Sorry, the money is not enough.")
        return False

    
def check(selected):
    for item in selected:
        if selected[item] >= resources[item]:
            print   (f"Sorry there isn't enough {item}")
            return False
        return True

def coffee(choice,selected):
    for item in selected:
        resources[item] -= selected[item]
    print(f"Here is your {choice}, Enjoy!")



should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappuccino)\n")
   
    if choice == "off":
        should_continue = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        selected_drink = MENU[choice]
        if check(selected_drink["ingredients"]):
            paid = pay()
            if change(selected_drink['cost'],paid):
                coffee(choice,selected_drink["ingredients"])
        


        
        