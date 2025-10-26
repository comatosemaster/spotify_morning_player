import os
import random
import datetime
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# load .env
load_dotenv()

scopes = "user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

results = sp.search(q=f"genre:'emo'", type="track", limit=50)
tracks = results["tracks"]["items"]

print(tracks)