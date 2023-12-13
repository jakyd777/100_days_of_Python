import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url)
page = response.text
content = BeautifulSoup(page, "html.parser")

films = content.find_all(name="h3", class_="listicleItem_listicle-item__title__hW_Kn")

film_list = [film.getText() for film in films[::-1]]  # [::-1] will reverse list with slice operator

with open("best_film2.txt", mode="w") as text_file:
    for movie in film_list:
       text_file.write(f"{movie}\n")

