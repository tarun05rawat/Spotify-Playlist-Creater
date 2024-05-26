from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
      client_id="b5b6fb8818984e7bae384e0f83ec2c6b",
      client_secret="bdb14b8a4e3f43709614c0fc2000b99c",
      redirect_uri="https://example.com",
      username="tarun",
      cache_path="token.txt",
      show_dialog=True,
      scope="playlist-modify-private",
    )
)

user_id = sp.current_user()["id"]


date = input("What year would you want to travel to? Type your answer in the YYYY-MM-DD format :: ")

response = requests.get("https://www.billboard.com/charts/hot-100/"+date)
contents = response.text

soup = BeautifulSoup(contents,"html.parser")

song_names = soup.select("li ul li h3")

song_names_list = [song.getText().strip() for song in song_names]

# for song in song_names_list:
#   # print(song)


song_names = song_names_list
song_uris =[]
year = date.split("-")[0]

for song in song_names:
  result = sp.search(q=f"track:{song} year:{year}", type="track")
  try:
    uri = result["tracks"]["items"][0]["uri"]
    song_uris.append(uri)
  except IndexError:
    print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard Top 100", public=False)



sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
print(playlist)





