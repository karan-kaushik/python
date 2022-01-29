import requests
from datetime import datetime
import pytz

MY_LAT = 19.1071
MY_LONG = 72.8368

def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_long = float(data["iss_position"]["longitude"])

    if (MY_LAT-5 <= iss_lat <= MY_LAT+5) and (MY_LONG-5 <= iss_long <= MY_LONG+5):
        return True
    else:
        return False    

def is_night():
    parameters = {
        "lat": MY_LAT, 
        "lng": MY_LONG,
        "formatted": 0,
        }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now(pytz.utc).hour

    if time_now >= sunset and time_now <= sunrise:
        return True
    else:
        return False
    
if is_iss_overhead() and is_night():
    print("It's overhead!")
else:
    print("It's not overhead!")