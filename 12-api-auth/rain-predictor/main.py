import requests

API_KEY = "XXXXX"
OWM_URL = "http://api.openweathermap.org/data/2.5/onecall"

weather_params = {
    "lat": 19.0144,
    "lon": 72.8479,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_URL, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
        
if will_rain:
    print("Bring an umbrella")
