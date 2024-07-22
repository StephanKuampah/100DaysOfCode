import requests
import datetime

LAT = 5.603717
LONG = -0.186964





parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}

date = datetime.datetime.now()
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)
print(date.hour)