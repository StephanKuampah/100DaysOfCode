student_scores = {
    "Harry":81,
    "Ron":78,
    "hermoine":99,
    "Draco":74,
    "Neville":62
}

student_grades = {}


for score in student_scores:
    if student_scores[score] >= 91:
        student_grades[score] = 'Outstanding'
    elif student_scores[score] >= 81 and student_scores[score]<= 90:
        student_grades[score] = 'Exceeds Expectations'
    elif student_scores[score] >= 71 and student_scores[score]<= 80:
        student_grades[score] = 'Acceptable'
    else:
        student_grades[score] = 'Fail'

print(student_grades)

 