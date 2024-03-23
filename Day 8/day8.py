# simple function
def greet():
    print("Hello World")
    print("Enjoy Coding?")
    print("Happy coding")

# function with input
def greet_with_input(name,location):
    print(f'hello {name}')
    print(f'do you enjoy coding at {location}')
    print(f'anyway happy coding {name} from {location}')

name = input('What is your name?\n')
location = input('Where do you live?\n')

greet_with_input(name,location)