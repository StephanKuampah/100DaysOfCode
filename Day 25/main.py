import turtle 
import pandas



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)


data = pandas.read_csv('50_states.csv')

states = data.state.to_list()

score = 0
mentioned = []


is_on = True

while is_on:
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt= "What's another state's name?").title()
    
    if (answer_state in states) and (answer_state not in mentioned):    
        score += 1
        name = turtle.Turtle()
        new = data[data.state == f"{answer_state}"]
        position = (new.x.iloc[0], new.y.iloc[0])
        name.penup()
        name.goto(position)
        name.write(f"{answer_state}")
        name.hideturtle()     
        mentioned.append(answer_state)
    elif (answer_state in mentioned):
        print("you already mentioned this state")
    
    elif answer_state == "Exit":
        is_on = False
        new_states = [states.remove(state) for state in states if state in mentioned]
        new_states = pandas.DataFrame(states)
        new_states.to_csv("states_to_learn.csv")
            
    else :
        print("State not valid")

    if score == 50:
        is_on = False
        print("contgratulations you mentioned all 50 states")
    






