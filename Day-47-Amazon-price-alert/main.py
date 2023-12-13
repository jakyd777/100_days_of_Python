import requests
from bs4 import BeautifulSoup
from pprint import pprint
import smtplib
import lxml

LIMIT_PRICE = 200.00
MY_EMAIL = "your.email@gmail.com"
EMAIL_PASS = "email_password"


def price_request():
    amazon_url = "https://www.amazon.com/dp/B075CWJ3T8?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1" # product you want to track
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
        "Accept-Language": "sk-SK,sk;q=0.9,cs;q=0.8,en-US;q=0.7,en;q=0.6,pl;q=0.5,it;q=0.4,de;q=0.3,ru;q=0.2"
    }
    response = requests.get(amazon_url, headers=header)
    data = response.text
    web_content = BeautifulSoup(data, "html.parser")
    price_data = web_content.find(name="span", class_="a-price-whole")
    price_fraction_data = web_content.find(name="span", class_="a-price-fraction")
    whole_price = float(f"{price_data.getText()}{price_fraction_data.getText()}")
    product_title_data = web_content.find(name="span", id="productTitle")
    product_title = product_title_data.getText().strip(" ")
    product_list = {
        "title": product_title,
        "price": whole_price
    }
    return product_list


def send_email(product_info: dict):
    my_email = MY_EMAIL
    password = EMAIL_PASS
    title = product_info["title"]
    price = product_info["price"]
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f'Subject:Amazon price ALERT!!\n\n Product: {title} has now price {price}'.encode("utf-8")
        )

def main():
    product_info = price_request()
    if product_info["price"] < LIMIT_PRICE:
        send_email(product_info)


if __name__ == '__main__':
    main()
