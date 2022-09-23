from twilio.rest import Client
import os
from twilio.http.http_client import TwilioHttpClient
import requests

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")

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
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="Bring an Umbrella",
        from_='+SECRETS',
        to='+SECRETS'
    )
    print(message.status)
else:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="No Umbrella Needed",
        from_='+SECRETS',
        to='+SECRETS'
    )
    print(message.status)