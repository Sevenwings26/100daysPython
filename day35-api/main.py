import requests

parameters = {
    "lat": 51.50735,
    "lon": -0.12758,
    "appid": "6e9139b8391a09da7139442b56ffd198",
    "cnt":4
}

url = "https://api.openweathermap.org/data/2.5/forecast"  # Added "https://"

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()

# get the first item id ---   
# print(data['list'][0]['weather'][0]['id']) 


will_rain = False
# get the id of the 4 cnt   
for hour_data in data["list"]:
    # for id_d in hour_data["weather"]:
    #     print(id_d["id"])
    # OR     
    # print(hour_data["weather"][0]["id"])
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("It's going to rain today. Bring an Umbrella")

