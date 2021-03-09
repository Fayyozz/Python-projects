from data_manager import DataManager
from flight_search import FlightSearch

flight_search = FlightSearch()
data_manager = DataManager()

sheet_data = data_manager.get_all_data()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        code = flight_search.get_code(row["city"])
        row["iataCode"] = code
        data_manager.update_code(row)

for destination in sheet_data:
    flight = flight_search.search_flight(destination["iataCode"])
    if flight.price < destination["lowestPrice"]:
        from notification_manager import NotificationManager
        notification_manager = NotificationManager(flight)
        notification_manager.send_message()





