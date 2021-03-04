import requests
from datetime import datetime

response_iss = requests.get("http://api.open-notify.org/iss-now.json")
iss_longitude = response_iss.json()["iss_position"]["longitude"]
iss_latitude = response_iss.json()["iss_position"]["latitude"]

MY_LAT = 41.299496
MY_LONG = 69.240074

my_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response_for_time = requests.get("https://api.sunrise-sunset.org/json", params=my_parameters)
sunrise = response_for_time.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response_for_time.json()["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()
hour_now = time_now.hour



