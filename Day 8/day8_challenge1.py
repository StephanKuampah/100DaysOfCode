# function goes here 
def paint_calc(height,width,cover):
    number_of_cans = round(((height * width)/cover))
    print(f"You'll need {number_of_cans} cans to paint.")



test_h = int(input("Height of wall\n"))
test_w = int(input("Weight of wall\n"))
coverage = 5
paint_calc(height=test_h,width=test_w,cover=coverage)
