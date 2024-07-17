from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

    

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps 
    window.after_cancel(timer)
    reps = 0
    task_label.config(text="Timer",font=(FONT_NAME, 50,"bold"), fg=GREEN,bg= YELLOW)
    canvas.itemconfig(time, text="00:00")
    check_label.config(text="",font=(FONT_NAME, 10,"bold"), fg=GREEN,bg= YELLOW)
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break = LONG_BREAK_MIN *  60
    short_break = SHORT_BREAK_MIN *  60
    if reps % 2 != 0:
        task_label.config(text="Work",font=(FONT_NAME, 50,"bold"), fg=GREEN,bg= YELLOW)
        count_down(work_sec)
    elif reps == 8:
        task_label.config(text="Break",font=(FONT_NAME, 50,"bold"), fg=RED,bg= YELLOW)
        count_down(long_break)
    else:
        task_label.config(text="Break",font=(FONT_NAME, 50,"bold"), fg=PINK,bg= YELLOW)
        
        count_down(short_break)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    if int(count_sec) < 10 and int(count_sec) > 0:
        count_sec = f"0{count_sec}"
        

    canvas.itemconfig(time, text=f"{count_min}:{count_sec}")
    if count > 0 :
        global timer
        timer = window.after(300, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_check = math.floor(reps/2)
        for _ in range(work_check):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=50,pady=50,bg=YELLOW)

image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
canvas.create_image(100,112, image=image)
time = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(row=1,column=1)






task_label = Label(text="Timer",font=(FONT_NAME, 50,"bold"), fg=GREEN,bg= YELLOW)
task_label.grid(row=0, column= 1)


start_button = Button(text="Start",highlightthickness=0, command= start_timer)
start_button.grid(row=2,column=0)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)

check_label = Label(text="",font=(FONT_NAME, 10,"bold"), fg=GREEN,bg= YELLOW)
check_label.grid(row=3, column= 1)


























window.mainloop()