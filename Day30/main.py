from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_generator():
    # initialising password variable to populate with for loop
    password_list = [choice(letters) for i in range(randint(8, 10))]
    password_list += [choice(symbols) for i in range(randint(2, 4))]
    password_list += [choice(numbers) for i in range(randint(2, 4))]

    # shuffling password characters
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0,END)
    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password":password
        }
    }
    if len(website) == 0:
        answer = False
        messagebox.showinfo(title="Error", message="sorry, website cannot be null")
    elif len(password) == 0:
        answer = False
        messagebox.showinfo(title="Error", message="sorry, password cannot be null")
    else:
        answer = messagebox.askokcancel(title=website, message=f"These are the details you entered: \nEmail: {email} \nPassword: {password} \nIs it okay to save?")
    if answer == True:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data) 
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file,indent=4)
        finally:
            website_entry.delete(0,END)
            password_entry.delete(0,END)

    
# ---------------------------- FIND PASSWORD ------------------------------- #
def search():  
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)  
                   
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website in data:
            email = data[website]["email"] 
            password = data[website]["password"]
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title=website, message=f"no details for {website} exists") 
       
        
            
        
    


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

image = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200)
canvas.create_image(100,100, image= image)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)
password_label = Label(text="Password")
password_label.grid(row=3,column=0)



website_entry = Entry(width=34)
website_entry.focus()
website_entry.grid(row=1,column=1)
email_entry = Entry(width=54)
email_entry.insert(0, "kuampahstephan@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)
password_entry = Entry(width=35)
password_entry.grid(row=3,column=1)


search_button = Button(text="Search",width=15,command=search)
search_button.grid(row=1,column=2)
generate_button = Button(text="Generate Password",command=password_generator)
generate_button.grid(row=3,column=2)
add_button = Button(text="Add", width=45, command=save)
add_button.grid(row=4,column=1,columnspan=2)
































window.mainloop()