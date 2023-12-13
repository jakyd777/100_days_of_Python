import requests
from bs4 import BeautifulSoup
new_url = "https://www.timeout.com/film/best-movies-of-all-time"
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(new_url)
page = response.text
content = BeautifulSoup(page, "html.parser")

films = content.find_all(name="h3", class_="_h3_cuogz_1")

film_list = [film.getText().split("\xa0")[1] for film in films[:-1]]
with open("best_film.txt", "w") as text_file:
    text = ""
    for index in range(len(film_list)):
        text = text + f"{index+1}. {film_list[index]}\n"
    text_file.write(text)
