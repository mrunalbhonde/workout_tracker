from datetime import datetime
import requests
from requests.auth import HTTPBasicAuth

APP_ID = "your_id"
API_KEY = "your_key"
YOUR_GENDER = "female"
YOUR_WEIGHT = 57
YOUR_HEIGHT = 155
YOUR_AGE = 20
USER_NAME = "authentication_username"
PASSWORD = "password_basicauthentication"

my_query = input("What workout did you do today?")
end_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}
request_body = {
     "query": f"{my_query}",
     "gender": YOUR_GENDER,
     "weight_kg": YOUR_WEIGHT,
     "height_cm": YOUR_HEIGHT,
     "age": YOUR_AGE
}

today = datetime.now()
date = today.strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
response = requests.post(url=end_url, json=request_body, headers=headers)
result = response.json()

sheety_endpoint = "https://api.sheety.co/ed29b0fff99f7d699d8afab74eb96d6f/myWorkoutDatabase/workouts"

for exercise in result["exercises"]:

    add_row_json = {
        "workout": {
            "date": date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint,
                               json=add_row_json,
                               headers=headers,
                               auth=(
                                    USER_NAME,
                                    PASSWORD
                               ))
print(sheet_response.text)