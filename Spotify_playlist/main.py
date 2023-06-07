import requests
from bs4 import BeautifulSoup


URL = "https://www.billboard.com/charts/hot-100/2010-07-03/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_songs = soup.find_all(name="li", class_="o-chart-results-list__item")
all_artists = soup.find_all(name="span")

song_titles = [song.getText for song in all_songs]


with open("songs.txt", mode="w", encoding="utf-8") as file:
    for title in song_titles:
        file.write(f"{title}\n")
