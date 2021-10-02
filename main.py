import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "11c0c2b8537f52b1cf1385cc61b7011b"
account_sid = "AC840599cfd9da10f42abf09c2bea301ba"
auth_token = "1eea6675c90630dbe12298b4bfc8aab8"
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
        from_='+15134333461',
        to='+917411318645'
    )
    print(message.status)

"""Below is my own method"""
# for i in range(0, 12):
#     weather_data_hourly = weather_data["hourly"][i]["weather"][0]["id"]
#     hourly_list.append(weather_data_hourly)
# print(hourly_list)
#
#
# for i in hourly_list:
#     if i < 700:
#         print("It will rain")
#         print(i)
#         break
#     else:
#         pass

