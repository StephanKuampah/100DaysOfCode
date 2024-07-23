import requests
from twilio.rest import client



# endpoint =  "https://api.openweathermap.org/data/2.5/weather"
endpoint  = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "a520f611de09cd24bf77a18f43de1524"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}

response = requests.get(endpoint,params=weather_params)
response.raise_for_status()
data = response.json()
data_slice = data["hourly"][:12]

will_rain = False 

for hour_data in data_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
if will_rain:
    print("Bring an umbrella")

