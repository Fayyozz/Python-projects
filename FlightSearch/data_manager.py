import requests

API_ENDPOINT = "https://api.sheety.co/a57e15114f768bcc78cd38d0d8c6280e/flightSearch/prices"


class DataManager:

    def get_all_data(self):
        response = requests.get(url=API_ENDPOINT)
        return response.json()["prices"]

    def update_code(self, row):
        body = {
            "price": {
                "iataCode": row["iataCode"]
            }
        }
        api_row_url = f"{API_ENDPOINT}/{row['id']}"
        requests.put(url=api_row_url, json=body)


