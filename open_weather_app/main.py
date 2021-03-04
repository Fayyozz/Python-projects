import requests
from twilio.rest import Client


api_key = "9b3519e8f912149b87bb1229c0694b63"
account_sid = "ACfc5672db37b86b7101318c7e6c69faff"
auth_token = "3dc06b2db42706941d487c370ba34440"


latitude = 41.299496
longitude = 69.240074
parameters = {
    "lat": latitude,
    "lon": longitude,
    "exclude": "minutely,daily,current",
    "appid": api_key,
}

response_weather = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response_weather.status_code)
response_weather.raise_for_status()

weather_data = response_weather.json()
next_12_hours = weather_data["hourly"][0:12]
weather_codes = [hour["weather"][0]["id"] for hour in next_12_hours if "id" in hour["weather"][0]]
print(weather_codes)

will_rain = False

for code in weather_codes:
    if code <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain today ☔☔☔ Please bring an umbrella!",
        from_='+19284474635',
        to='+998915228512'
    )

    print(message.status)