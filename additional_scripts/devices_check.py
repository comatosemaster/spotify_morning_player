import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv

load_dotenv()

# playback scopes py variable
scopes = "user-read-playback-state user-modify-playback-state"

# scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

# setting up py variable from API devices
devices = sp.devices()["devices"]

# check active devices or print No devices found if there are not any
if not devices:
    print("⚠️  No devices found. Open Spotify on your PC or phone and start any song for a second, then rerun.")
else:
    print("✅ Devices detected:")
    for d in devices:
        print(f"- {d['name']} type={d['type']} active={d['is_active']}")