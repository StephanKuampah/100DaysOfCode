import smtplib
import datetime
import pandas
from random import *


entry = 0
my_email = "amankwaemannuela@gmail.com"
password = "steph1rada"

Names = ["Mum","Dad","Sister"]
Emails = ["mum@gmail.com","dad@gmail.com","sister@gmail.com"]
Years = ["1970", "1965","1998"]
Days = ["24","20","25"]
Months = ["1","7","5"]



##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv
birthdays = pandas.read_csv("birthdays.csv")

birthday_list = birthdays.to_dict()

for name,email,year,day,month in zip(Names,Emails,Years,Days,Months):
    entry += 1
    birthday_list['name'][entry] = name
    birthday_list['email'][entry] = email
    birthday_list['year'][entry] = year
    birthday_list['day'][entry] = day
    birthday_list['month'][entry] = month

updated_birthdays = pandas.DataFrame(birthday_list)

updated_birthdays.to_csv('birthdays.csv', index=False)

now = datetime.datetime.now()
day_chosen = now.day
month_chosen = now.month
chosen_letter = str(randint(1,3))



# 2. Check if today matches a birthday in the birthdays.csv
for index,row in updated_birthdays.iterrows():
    if row['day'] == str(day_chosen) and row['month'] == str(month_chosen):
        name_chosen = row['name']
        email_chosen = row['email']
        send_mail = True
        break
    else:
        send_mail = False
              
if send_mail:
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(f"letter_templates/letter_{chosen_letter}.txt") as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", f"{name_chosen}")
    # 4. Send the letter generated in step 3 to that person's email address.
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email,  password=password)
            connection.sendmail(from_addr=my_email,     to_addrs=f"{email_chosen}", msg=f"{new_letter}")
    except Exception as e:
        print(e)
    else:
        print(f"Email sent to {name_chosen} with email {email_chosen} successfully")
else:
    print("no birthdays today")
        

        
    

