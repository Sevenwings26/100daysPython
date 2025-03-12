import requests
from twilio.rest import Client

account_sid = "AC4914033bcc83f7c3e31c11e7856fa6bb"
auth_token = "5cdc91d8c6d7c922d6ebe9f7056722fd"
test_auth_token = "57898ad823d422c3d3b42f5784a069a1"
api_key = "SK23763700c929f5b905a4b9ab0dd9e415"
secret_key = "QBblswpHkbato9GDwd0h4K4R2sJTS6jf"

parameters = {
    "lat": 51.50735,
    "lon": -0.12758,
    "appid": "6e9139b8391a09da7139442b56ffd198",
    "cnt":4
}

url = "https://api.openweathermap.org/data/2.5/forecast" 

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

# get the first item id ---   
# print(data['list'][0]['weather'][0]['id']) 


will_rain = False
# get the id of the 4 cnt   
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # twilio messager   
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain soon, stay dry!",
            from_='+12345162657',
            to='+2349067442825'

            # use whatapp
        )

print(message.status)
