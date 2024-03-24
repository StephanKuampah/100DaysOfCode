h = float(input("what is your height in cm?\n"))
w = float(input("what is your weight in kg?\n"))
result = round(w/h**2)
if result < 18.5:
    print(f"Your BMI is {result},you are underweight.")
elif result <= 25:
    print(f"Your BMI is {result},you are,you are of normal weight")
elif result <= 30:
    print(f"Your BMI is {result},you are overweight")
elif result <= 35:
    print(f"Your BMI is {result},you are obese")
else:
    print(f"Your BMI is {result},you are clinically obese")
