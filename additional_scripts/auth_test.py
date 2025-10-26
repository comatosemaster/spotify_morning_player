import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv

# load .env
load_dotenv()

# build an auth manager
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope="user-read-email"
))

me = sp.current_user()

print("✅ Auth OK. Logged in as:", me["display_name"], f"({me['id']})")