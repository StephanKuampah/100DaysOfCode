from tkinter import *

window = Tk()

window.title("My first Gui program")
window.minsize(width=500, height=300)



my_label = Label(text="Hello" , font=("Arial", 24, "bold"))
my_label.grid(row=0,column=0)

def button_clicked():
    my_label.config(text=f"{input.get()}")

button = Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)

new_button = Button(text="New Button")
new_button.grid(row=0,column=2)

input = Entry(width=40)
input.grid(row=2,column=3)



















window.mainloop()