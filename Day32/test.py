import smtplib
import datetime
from random import *


my_email = "amankwaemannuela@gmail.com"
password = "steph1rada"




with open("quotes.txt") as file:
    quote_file = file.readlines()

quotes = []
for quote in quote_file:
    new_quote = quote.strip("\n''")
    quotes.append(new_quote)
    
random_quote = choice(quotes)

date = datetime.datetime.now()
day = date.weekday()

if day == 5:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,         password=password)
        connection.sendmail(from_addr=my_email,     to_addrs="kuampahstephan@gmail.com", msg=f" {random_quote}")
    


