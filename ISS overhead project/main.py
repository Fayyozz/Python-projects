import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "00010847f@gmail.com"
MY_PASSWORD = "61251526"
TO_EMAIL = "fayyoz01@outlook.com"

MY_LAT = 41.299496
MY_LONG = 69.240074


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    my_lat_min = MY_LAT - 5
    my_lat_max = MY_LAT + 5

    my_long_min = MY_LONG - 5
    my_long_max = MY_LONG + 5

    if my_lat_min < iss_latitude < my_lat_max and my_long_min < iss_longitude < my_long_max:
        return True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response_time = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response_time.raise_for_status()
    data_time = response_time.json()
    sunrise = int(data_time["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data_time["results"]["sunset"].split("T")[1].split(":")[0])

    time_now_hour = datetime.now().hour

    if time_now_hour > sunset or time_now_hour < sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        print("Success")
        with smtplib.SMTP("smtp.gmail.com", port=578) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL,
                                msg="Subject: International Space Station\n\n ISS came close. "
                                    "look "
                                    "up right now!")
