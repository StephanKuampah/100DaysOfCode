import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

my_email = "amankwaemannuela@gmail.com"
password = "steph1rada"


#Your position is within +5 or -5 degrees of the ISS position.
def overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    current_position_latitude = float(MY_LAT)
    current_position_longitude = float(MY_LONG)
    if (iss_latitude >= current_position_latitude -5 and iss_latitude <= current_position_latitude + 5) and (iss_longitude >=   current_position_longitude -5 and iss_longitude <= current_position_longitude + 5):
        return True






# and it is currently dark
def dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True




while True:
    # BONUS: run the code every 60 seconds.
    time.sleep(60)
    
    #If the ISS is close to my current position and dark
    if overhead() and dark():
        # Then send me an email to tell me to look up.    
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email,  password=password)
                connection.sendmail(from_addr=my_email,     to_addrs="dad@gmail.com", msg="Look up")
        except Exception as e:
            print(e)
            print("message to send is look up")
        else:
            print("Email sent")
    else:
        print("ISS not in range")





