import requests, time
from datetime import datetime, timezone
import smtplib

my_email= "SECRET EMAIL"
my_password= "SECRET CODE"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    my_longitude = -87.629799
    my_latitude = 41.878113

    if (my_latitude - 5 <= iss_latitude <= my_latitude + 5) and (my_longitude - 5 <= iss_longitude <= my_longitude + 5):
        return(True)

def is_night():
    parameter = {
        "lat":41.878113,
        "lng":-87.629799,
        "formatted":0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split('T')[1].split(':')[0])
    sunset = int(data["results"]["sunset"].split('T')[1].split(':')[0])

    time_now = datetime.now(timezone.utc)
    hour_now = time_now.hour
    if sunset < hour_now < sunrise:
        return (True)
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr="ISS Checker",
                                to_addrs="SECRET EMAIL",
                                msg=f"Subject: ISS Is Crossing Over\n\nThis is your notification that the ISS is passing over.")