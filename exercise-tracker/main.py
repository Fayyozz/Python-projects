import requests
from datetime import datetime

MY_HEIGHT = 1.80
MY_WEIGHT = 90.00
MY_AGE = 20
MY_GENDER = "male"

exercise_text = input("What exercise did you do today? ")

API_KEY = "595754d90d56f2f6bbeb655974fd510f"
APP_ID = "9a20e518"

api_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}
API_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

request_body = {
 "query": exercise_text,
 "gender": MY_GENDER,
 "weight_kg": MY_WEIGHT,
 "height_cm": MY_HEIGHT,
 "age": MY_AGE
}

exercise_response = requests.post(url=API_END_POINT, json=request_body, headers=api_headers)
result = exercise_response.json()

WORK_OUT_API_ENDPOINT = "https://api.sheety.co/a57e15114f768bcc78cd38d0d8c6280e/workoutTracking/workouts"
WORKOUT_TOKEN = "afunvufgrejhrftgerhlfgilhergihrfgljerhgliergherkljfuigbr"
USERNAME_AUTH = "fayyozz"
PASSWORD_AUTH = "fbfbfbfb"
headers = {"Authorization": f"Bearer {WORKOUT_TOKEN}"}

for exercise in result["exercises"]:
    date = datetime.now().strftime("%d/%m/%Y")
    time_now = datetime.now().strftime("%X")
    duration_min = exercise["duration_min"]
    calories_burnt = exercise["nf_calories"]
    exercise_name = exercise["name"]

    workout_body = {
        "workout": {
            "date": date,
            "time": time_now,
            "exercise": exercise_name.title(),
            "duration": duration_min,
            "calories": calories_burnt
        }
    }
    res = requests.post(url=WORK_OUT_API_ENDPOINT, json=workout_body, auth=(USERNAME_AUTH, PASSWORD_AUTH))
    print(res.text)



