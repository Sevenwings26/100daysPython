import spotipy 
from spotipy.oauth2 import SpotifyOAuth

# scope = (
#     scope="playlist-modify-private",
#     client_id = "a1f5c9e508304bb59fa2f456b6541192",
#     client_secret = "cc07d245e57645b7a47cd12488bb451d",
#     redirect_url = "http://example.com",
#     show_dialog=True,
#     cache_path="token.txt",
#     username = Iarowosola
# )

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id = "a1f5c9e508304bb59fa2f456b6541192",
        client_secret = "cc07d245e57645b7a47cd12488bb451d",
        redirect_uri = "http://example.com",
        show_dialog=True,
        cache_path="token.txt",
        username = "Iarowosola",
    )
)

user_id = sp.current_user()['id']

