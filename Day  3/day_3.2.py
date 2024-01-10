#BMI calculator
height = float(input("what is your height in m:\n"))
weight = float (input("what is your weight in kg:\n"))

h = height
w = weight
BMI = round(w / h**2)

if BMI < 18.5 :
    print (f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"your BMI is {BMI}, you are normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI}, you are overweight")
elif BMI < 35:
    print(f"your BMI is {BMI}, you are obese")
else:
    print(f"your weight is {BMI}, you are clinically obese")
