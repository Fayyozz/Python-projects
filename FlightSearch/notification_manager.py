
from twilio.rest import Client
from flight_data import FlightData

account_sid = 'ACfc5672db37b86b7101318c7e6c69faff'
auth_token = '4b49dbf9c08d7c6d28c5b3b641752b79'
client = Client(account_sid, auth_token)


class NotificationManager:

    def __init__(self, flight: FlightData):
        self.flight_info = flight

    def send_message(self):
        message = client.messages.create(
            body=f"Low Price Alert! Only £{self.flight_info.price} "
                 f"to fly from {self.flight_info.departure_city}-{self.flight_info.departure_airport_code} to"
                 f"{self.flight_info.toCity}-{self.flight_info.toCity_code}, from {self.flight_info.departure_date} to {self.flight_info.return_date}.",
            from_='+19284474635',
            to='+998915228512'
        )

        print(message.sid)
