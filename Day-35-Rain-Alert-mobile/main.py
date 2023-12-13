import requests
import os
from twilio.rest import Client

api_key = "147c1137da57a4d27ad84984e67d60dd"  # obtain from api openweathermap.com
url1= "https://api.openweathermap.org/data/2.5/forecast"  #endpoint for API

account_sid = "sid from twilio"  #SID from twilio.com"    #
auth_token = "token from twilio"  #"TOKEN from twilio.com"


PARAMETERS = {
    "lat": "49.002468",
    "lon": "21.239679",
    "appid": api_key,
}

will_rain = False

response = requests.get(url1, params=PARAMETERS)
response.raise_for_status()
data = response.json()

list_of_codes = [data["list"][x]["weather"][0]["id"] for x in range(4)]  # slice whole json to just info we need
for code in list_of_codes:
    if code < 700:      # weather codes when it will be rain
        will_rain = True
if will_rain:
    print("Bring an Umbrella")
# for x in range(39):
#     code = data["list"][x]["weather"][0]["id"]
#     print(code)
#     if code < 700:
#         print("Take an umbrella")
    # sending sms using twilio.com
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                        body="It's going to rain. Don't forget to take an umbrella☔",
                        from_="+1 twilio number",  # number got from twilio
                        to="+421 your number", # your number but must be verified by twilio
                    )
    print(message.status)

# last put code to server and run it every day at 0700 to get info when it's going to rain
