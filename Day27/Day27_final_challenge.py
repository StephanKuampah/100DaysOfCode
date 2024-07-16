from tkinter import *

window = Tk()

window.title("Mile to KM Converter")
window.config(padx=20,pady=20)

KM = 0

input = Entry(width=15)
input.grid(row=0,column=1)

mile_label = Label(text="Miles",font=("Arial", 10, "bold"))
mile_label.grid(row=0,column=2)

equal_label = Label(text="is equal to",font=("Arial", 10, "bold"))
equal_label.grid(row=1,column=0)


calculated_label = Label(text=f"{KM}",font=("Arial", 10, "bold"))
calculated_label.grid(row=1,column=1)

kilometer_label = Label(text="Km",font=("Arial", 10, "bold"))
kilometer_label.grid(row=1,column=2)

def calculate():
    mile = input.get()
    kilometer = round(float(mile) * 1.609)
    calculated_label.config(text=f"{kilometer}",font=("Arial", 10, "bold"))

button = Button(text="Calculate", command=calculate)
button.grid(row=2,column=1)





















window.mainloop()