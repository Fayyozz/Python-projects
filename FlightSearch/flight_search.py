import requests
from flight_data import FlightData
import datetime
API_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
API_KEY = "R4cz0DdSEZZ2qiJEqfH-lphcMU00Gjaq"
FLY_FROM = "LON"

class FlightSearch:

    def __init__(self):
        self.search_time_interval = (datetime.datetime.now(), datetime.datetime.now() + datetime.timedelta(days=6 * 30))

    def get_code(self, city_name):
        header = {
            "apikey": API_KEY
        }
        params = {
            "term": city_name,
            "location_types": "city",
            "limit": 1
        }
        response = requests.get(url=API_ENDPOINT, params=params, headers=header)
        code = response.json()["locations"][0]["code"]
        return code

    def search_flight(self, code):

        params = {
            "fly_from": FLY_FROM,
            "fly_to": code,
            "date_from": self.search_time_interval[0].strftime("%d/%m/%Y"),
            "date_to": self.search_time_interval[1].strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP"
        }
        header = {
            "apikey": API_KEY
        }
        url_api = "https://tequila-api.kiwi.com/v2/search"
        response = requests.get(url=url_api, params=params, headers=header)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {code}")
            return None

        flight_data = FlightData(departure_city=data["cityFrom"],
                                 departure_airport_code=data["cityCodeFrom"],
                                 toCity=data["cityTo"],
                                 toCity_code=data["cityCodeTo"],
                                 departure_date=data["route"][0]["local_departure"].split("T")[0],
                                 return_date=data["route"][1]["local_departure"].split("T")[0],
                                 price=data["price"])
        return flight_data




