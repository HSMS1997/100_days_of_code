import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "hilansms@gmail.com"
MY_PASSWORD = "fatimajosmar"

MY_LNG = -46.633308
MY_LAT = -23.550520


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])
    # iss_position = (iss_longitude, iss_latitude)

    if 18 < iss_latitude < 28 and 41 < iss_longitude < 51:
        return True


##### YOUR POSITION #####


def is_night():
    parameters = {
        "Lat": MY_LAT,
        "Lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(" https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1])
    sunset = int(data["results"]["sunset"].split("T")[1])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )
