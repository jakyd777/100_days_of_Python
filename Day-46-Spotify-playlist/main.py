
SPOTIPY_CLIENT_ID = 'Your client ID'
SPOTIPY_CLIENT_SECRET = 'Your client secret'
SPOTIFY_DISPLAY_NAME = 'your spotify name'

from pprint import pprint
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup

def clean_text(text):
    list = [char for char in text]
    #print(list)
    new_list = [item for item in list if item != "\n"]
    new_list_2 = [item for item in new_list if item != "\t"]

    string = ""
    for char in new_list_2:
        string += char
    return string


date = input("Which year do you wont to travel to? Type the date in this format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(url)
data = response.text
content = BeautifulSoup(data, "html.parser")

songs_100_list = []
songs = content.find_all(class_="o-chart-results-list-row")

titles = [song.h3.getText() for song in songs]
clean_titles = []
for title in titles:
    clean_title = clean_text(title)
    clean_titles.append(clean_title)
#print(len(clean_titles))

singers = [song.h3.next_sibling.next_sibling.getText() for song in songs]
clean_singers = []
for singer in singers:
    clean_singer = clean_text(singer)
    clean_singers.append(clean_singer)
#print(len(clean_singers))

for x in range(len(clean_titles)):
    new_data = {
        "title": clean_titles[x],
        "singer": clean_singers[x]
    }
    songs_100_list.append(new_data)


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username=SPOTIFY_DISPLAY_NAME,
            )
        )
        #search
uri_list = []
for song in songs_100_list:
    title = song["title"]
    singer = song["singer"]
    try:
        result = sp.search(q=f"track: {title}, artist:{singer}", type="track")
        uri = result['tracks']['items'][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        print(f"{title} doesn't exist in Spotify. Skipped.")
print(uri_list)
user_id = sp.current_user()["id"]

song_uris = ["The list of", "song URIs", "you got by", "searching Spotify"]

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
# print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=uri_list)
