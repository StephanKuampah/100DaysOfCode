import requests
import datetime

USERNAME = "ghostshot"
TOKEN = "0Zez#DNeU45Qt*!"
GRAPH_ID = "code1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes"
}

response = requests.post(pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "coding tracker",
    "unit": "mins",
    "type": "int",
    "color": "momiji"

}

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.post(graph_endpoint, json=graph_params, headers= headers)

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"



today = datetime.datetime.now()
pixel_params = {
    "date": f"{today.strftime("%Y%m%d")}",
    "quantity": "0"
}

response = requests.post(pixel_endpoint,json=pixel_params, headers= headers)
print(response.text)