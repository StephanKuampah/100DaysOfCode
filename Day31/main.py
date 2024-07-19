from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words={}


try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")




def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(words)
    canvas.itemconfig(current_language, text="French",fill="black")
    canvas.itemconfig(current_word, text=f"{current_card["French"]}",fill="black")
    canvas.itemconfig(current_image,image=card_front)
    flip_timer= window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(current_image,image=card_back)
    canvas.itemconfig(current_language, text="English",fill="white")
    canvas.itemconfig(current_word, text=f"{current_card["English"]}",fill="white")

def is_known():
    words.remove(current_card)
    words_to_learn = pandas.DataFrame(words)
    words_to_learn.to_csv("data/words_known.csv",index=False)
    next_card()


window = Tk()
window.title("Flash Card App")
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000,func=flip_card)



card_front = PhotoImage(file="images/card_front.png")

card_back = PhotoImage(file="images/card_back.png")

right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
current_image = canvas.create_image(400,263, image=card_front)
current_language = canvas.create_text(400,150, text="Title",font=("Ariel",30,"italic"))
current_word = canvas.create_text(400,263, text="Word",font=("Ariel",50,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=3)


right_button = Button(image=right,highlightthickness=0,command=is_known)
right_button.grid(row=2,column=2)

wrong_button = Button(image=wrong,highlightthickness=0,command=next_card)
wrong_button.grid(row=2,column=0)

next_card()


window.mainloop()