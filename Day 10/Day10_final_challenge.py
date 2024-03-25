# clear terminal
import os

def clear_terminal():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

from art import logo


# Add function
def add(n1,n2):
    return n1 + n2

# subtract function
def subtract(n1,n2):
    return n1 - n2

# divide function
def divide(n1,n2):
    return n1 / n2

# multiply functiom
def multiply(n1,n2):
    return n1 * n2


def calc():
    # logo
    print(f'{logo}\n')

    # start calculating
    n1 = float(input("What is the first number?\n"))

    # dictionary for operators
    operators = {'+':add, '-' : subtract, '*' : multiply, '/' : divide}

    for symbol in operators:
        print(symbol)


    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation symbol from the line above\n")

        n2 = float(input("What is the next number?\n"))

        answer = operators[operation_symbol](n1,n2)

        print(f"{n1} {operation_symbol} {n2} = {answer}")

        to_continue = input("Would you like to continue calculating? Type 'Yes' to continue or 'no' to start a new calculation\n")
        if to_continue == 'yes':
            n1 = answer

        else:
            should_continue = False
            clear_terminal()
            calc()
    
calc()