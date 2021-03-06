import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "Your API Key"
account_sid = "Your account_sid"
auth_token = "Your auth_token"
latitude = 53.551086
longitude = 9.993682
hourly_list = []

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
print(weather_data)
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True

if will_rain:
    # print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='Sender number',
        to='Your Number'
    )
    print(message.status)

