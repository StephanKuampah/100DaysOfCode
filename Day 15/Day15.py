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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def money(quarter, dime,nickel,penny):
    quarters = 0.25 * quarter
    dimes = 0.1 * dime
    nickels = 0.05 * nickel
    pennies = 0.01 * penny
    total = quarters + dimes + nickels + pennies
    return total

def change(cost,paid):
    change = paid - cost
    return(change)

def ingredient_tracking():
    money = 0
    water = resources['water'] - MENU[f"{choice}"]["ingredients"]["water"]
    milk = resources['milk'] - MENU[f"{choice}"]["ingredients"]["milk"]
    coffee = resources['coffee'] - MENU[f"{choice}"]["ingredients"]["coffee"]
    money += cost
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${cost}")

# def ingredient_tracking():
#     money = 0
#     a = MENU[f"{choice}"]["ingredients"]["water"]
#     b = MENU[f"{choice}"]["ingredients"]["milk"]
#     c = MENU[f"{choice}"]["ingredients"]["coffee"]
#     if a != "" and b != "" and c != "" and cost != "":
#         water = resources['water'] - a
#         milk = resources['milk'] - b
#         coffee = resources['coffee'] - c
#         money += cost
#     else:
#         water = resources['water'] - 0
#         milk = resources['milk'] - 0
#         coffee = resources['coffee'] - 0
#         money
#     print(f"Water: {water}ml")
#     print(f"Milk: {milk}ml")
#     print(f"Coffee: {coffee}g")
#     print(f"Money: ${cost}")



# ingredient_tracking()


should_continue = True
while should_continue:
    choice = input("What would you like? (espresso/latte/cappucino)\n")
    cost = MENU[f"{choice}"]['cost']
    print("Please insert coins.")
    quarter = float(input("How many quarters?: "))
    dime = float(input("How many dimes?: "))
    nickel = float(input("How many nickels?: "))
    penny = float(input("How many pennies?: "))
    money_total = round(money(quarter,dime,nickel,penny),2)
    change = change(cost,money_total)
    print(f"Here is ${change} in change")
    print(f"Here is your {choice}, Enjoy!")