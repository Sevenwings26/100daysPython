import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scrape Billboard Hot 100
url = "https://www.billboard.com/charts/hot-100/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

response = requests.get(url, headers=headers)
wb_page = response.text
bsoup = BeautifulSoup(wb_page, "html.parser")

hot_list = bsoup.find("div", {"class": "chart-results-list"})
if not hot_list:
    print("Could not find the chart-results-list div.")
    exit()

music_box = hot_list.find_all("div", {"class": "o-chart-results-list-row-container"})

song_titles = []
for music in music_box:
    if music:
        title_tag = music.find("h3", {"id": "title-of-a-story"})
        if title_tag:
            song_titles.append(title_tag.text.strip())

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id="a1f5c9e508304bb59fa2f456b6541192",
        client_secret="cc07d245e57645b7a47cd12488bb451d",
        redirect_uri="https://example.com",  # ✅ Use HTTPS
        show_dialog=True,
        cache_path="token.txt",
        username="Iarowosola",
    )
)

# Get User ID
user_id = sp.current_user()["id"]

# Search for tracks on Spotify
track_uri_list = []
for song in song_titles:
    search_results = sp.search(q=song, type="track", limit=1)
    try:
        track_uri = search_results["tracks"]["items"][0]["uri"]
        track_uri_list.append(track_uri)
    except IndexError:
        print(f"Track '{song}' not found on Spotify.")

# Create Playlist
playlist = sp.user_playlist_create(
    user=user_id,
    name="Billboard Hot 100 Playlist",
    public=False,
    description="Automatically generated Billboard Hot 100 playlist."
)

# Add Tracks to Playlist
playlist_id = playlist["id"]
sp.playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_uri_list)
print("Tracks successfully added to the playlist!")
