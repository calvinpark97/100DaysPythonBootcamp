from twilio.rest import Client
import requests

api_key = "612dfdf19f81cb2709a6fb175b5be609"
account_sid = 'ACf2d017588e424bc4dbfcaa105e8c7c26'
auth_token = '6b78ff2dfa4e61484bd3ec714753b347'

PARAMETERS = {
    "lat": "42.1392",
    "lon": "-87.92895",
    "appid": api_key,
    "units": "imperial",
    "exclude": "current,minutely,daily"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
print(response.status_code)
data=response.json()


will_rain = False
weather_slice = (data["hourly"][:12])
for weather_data in weather_slice:
    if weather_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an Umbrella",
        from_='+14029233602',
        to='+12246235007'
    )
    print(message.status)