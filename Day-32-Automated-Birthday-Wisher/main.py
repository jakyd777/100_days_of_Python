import random
import pandas as pd
import smtplib
import datetime as dt

now = dt.datetime.now()
now_month = now.month
now_day = now.day


def send_email(email, name):
    ran_num = random.randint(1, 3)
    my_email = "your.email@gmail.com"
    my_password = "email_account_password "
    with open(f"letter_templates/letter_{ran_num}.txt") as letter_file:
        text_letter = letter_file.read()
        new_text = text_letter.replace("[NAME]", f"{name}")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:HAPPY BIRTHDAY\n\n{new_text}"
        )


data = pd.read_csv("birthdays.csv")
data_list = data.to_dict(orient="records")
for each_name in data_list:
    if each_name["month"] == now_month:
        if each_name["day"] == now_day:
            send_email(each_name["email"], each_name["name"])
