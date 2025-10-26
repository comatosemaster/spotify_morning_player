import os
from spotipy.oauth2 import SpotifyOAuth
import spotipy
from dotenv import load_dotenv
import random

# load .env
load_dotenv()

# playback scopes py variable
scopes = "user-read-playback-state user-modify-playback-state"

# scopes
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

# py variable containing track uri to be played
track_uris = [
    "spotify:track:4uLU6hMCjMI75M1A2tKUQC",  # Never Gonna Give You Up
    "spotify:track:2nLtzopw4rPReszdYBJU6h",  # Numb
    "spotify:track:60a0Rd6pjrkxjPbaKzXjfq",  # In the End
    "spotify:track:3AJwUDP919kvQ9QcozQPxg"   # Shape of You
]

random_track = random.choice(track_uris)

track_info = sp.track(random_track)
track_name = track_info["name"]
artists = ", ".join([artist["name"] for artist in track_info["artists"]])

# setting up py variable from API devices
devices = sp.devices()['devices']

# exit if there are no any devices found
if not devices:
    raise SystemExit("⚠️ No devices found. Open Spotify and play something once.")

# checks for active device and assigns device variable active_device's value
active_device = None

for d in devices:
    if d["is_active"]:
        active_device = d
        break

if active_device is None:
    active_device = devices[0]

device = active_device

# starts playback
sp.transfer_playback(device_id=device["id"], force_play=True)
sp.start_playback(uris=[random_track])

print(f"Playing now: {artists} - {track_name}")

print(f"✅ Playing on: {device['name']}")