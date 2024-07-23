from tkinter import *
from quiz_brain import *
import time

THEME_COLOR = "#375362"


class QuizGui:
    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250,highlightthickness=0)
        self.question_text = self.canvas.create_text(150,125,width=280,text="question",font=("Arial",20,"italic"),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2)
        self.right_image = PhotoImage(file="images/true.png")
        self.wrong_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=self.right_image,highlightthickness=0,command=self.right)
        self.true_button.grid(row=2,column=0,pady=20)
        self.false_button = Button(image=self.wrong_image,highlightthickness=0,command=self.wrong)
        self.false_button.grid(row=2,column=1,pady=20)
        self.score_label = Label(text=f"Score: {self.quiz.score}",bg=THEME_COLOR)
        self.score_label.config(pady=20,fg="white")
        self.score_label.grid(row=0,column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.score_label.config(text=f"Score: {self.quiz.score}")
        if self.quiz.still_has_questions():   
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've completed the quiz\n Your final score was: {self.quiz.score}/{self.quiz.question_number}",font=("Arial",15,"bold"))
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def right(self):
        self.user_answer = "True"
        answer = self.quiz.check_answer(self.user_answer)
        self.feedback(answer)
        
        

    def wrong(self):
        self.user_answer = "False"
        answer = self.quiz.check_answer(self.user_answer)
        self.feedback(answer)
        
    def feedback(self,answer):
        if answer == True:
            self.canvas.config(bg="green")   
        else:
            self.canvas.config(bg="red")   
        self.window.after(1000,self.get_next_question)















    
