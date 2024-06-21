from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
cash_register = MoneyMachine()
coffee_maker = CoffeeMaker()


should_continue = True
while should_continue:
    choices = menu.get_items()
    choice = input(f"What would you like? {choices}: ")
    if choice == "off":
        should_continue = False
    elif choice == "report":
        coffee_maker.report()
        cash_register.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if cash_register.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
