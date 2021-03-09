from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
users_data = data_manager.get_users()
print(users_data)
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price}" \
                  f" to fly from {flight.origin_city}-{flight.origin_airport}" \
                  f" to {flight.destination_city}-{flight.destination_airport}," \
                  f" from {flight.out_date} to {flight.return_date}."
        if flight.stop_overs > 0:
            message += f"\n Flight has {flight.stop_overs} stop overs via {flight.vie_city}."
            print(message)
        notification_manager.send_sms(message)
        for user in users_data:
            google_link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"
            email_message = f"Subject: Hello {user['firstName']}, \n\n"
            email_message = email_message + message + "\n" + google_link
            email_message = email_message.encode("utf-8")
            email = user["email"]
            notification_manager.send_email(email, email_message)







