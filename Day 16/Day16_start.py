from turtle import Turtle, Screen

screen = Screen()
tata = Turtle()
print(tata)
tata.shape('turtle')
tata.color('coral')

screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu","Squirtle","Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])
table.align = "c"
print(table)