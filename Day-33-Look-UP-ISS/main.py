import requests
import smtplib
from datetime import datetime
import time

# MY_LAT = 49.002468
# MY_LONG = 21.239679
MY_LAT = -5.002468
MY_LONG = 5.239679


def send_email():
    my_email = "your.email77@gmail.com"
    my_password = "your email account password"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:ISS\n\nTime to Look UP."
        )


def get_iss():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    iss_long = float(iss_data["iss_position"]["longitude"])
    iss_lat = float(iss_data["iss_position"]["latitude"])

    position_tuple = (iss_long, iss_lat)
    return position_tuple


def main():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])  #will split full format and get only hour
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    iss_long = get_iss()[0]
    iss_lat = get_iss()[1]

    if MY_LONG - 5 <= iss_long <= MY_LONG + 5 and MY_LAT - 5 < iss_lat < MY_LAT +5:
        if time_now > sunset or time_now < sunrise:
            send_email()
    time.sleep(60)
    main()


main()
