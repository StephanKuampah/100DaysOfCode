class QuizBrain:
    def __init__(self,q_list):
        self.question_number = 0
        self.current_score = 0
        self.question_list  = q_list
    
    def still_has_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print('You completed the game')
            return False
    
    
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} (True\False): ")
        self.answer_check(answer,current_question.answer)

    def answer_check(self,answer,correct_answer):   
         if answer.lower() == correct_answer.lower():
              self.current_score += 1
              print("You got it right!")
              print(f"The correct answer was: {correct_answer}.")
              print(f"Your score is: {self.current_score}/{self.question_number}")
         else:
              print("You got it wrong!")
              print(f"The correct answer was: {correct_answer}.")
              print(f"Your score is: {self.current_score }/{self.question_number}")

        

    

