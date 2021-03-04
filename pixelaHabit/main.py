import requests
from datetime import datetime
USERNAME = "fayyozbek"
TOKEN = "dfghekljhdusvdngvslvghvg"
PIXELA_END_POINT = "https://pixe.la/v1/users"
GRAPH_ID = "mygraph1"
pixela_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response  = requests.post(url=PIXELA_END_POINT, json=pixela_params)
# print(response.text)
graph_params = {
    "id": GRAPH_ID,
    "name": "My Habit for Coding!",
    "unit": "hours",
    "type": "int",
    "color": "ichou"
}
graph_endpoint = f"{PIXELA_END_POINT}/{USERNAME}/graphs"
graph_auth = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_auth)
# print(response)
today = datetime(year=2021, month=3, day=3)
pixel_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9",
}

# response = requests.post(url=pixel_graph_endpoint, json=pixel_params, headers=graph_auth)
# print(response)
update_param = {
    "quantity": "8"
}
update_endpoint = f"{pixel_graph_endpoint}/{today.strftime('%Y%m%d')}"
# d = requests.put(url=update_endpoint, json=update_param, headers=graph_auth)
# print(d.text)
d = requests.delete(url=update_endpoint, headers=graph_auth)
print(d.text)