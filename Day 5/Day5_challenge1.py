student_height = input("Input a list of student heights\n").split()
for n in range (0, len(student_height)):
    student_height[n] = int(student_height[n])
print(student_height)

height = 0
number = 0
for heights in student_height:
    height += heights
    number += 1
average = round(height/number)
print(average)