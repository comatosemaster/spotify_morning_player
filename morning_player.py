import os
import random
import datetime
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# load .env
load_dotenv()

# handling scopes
scopes = "user-read-playback-state user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scopes))

# configuration
user_genres = ["deathcore"]
log_file = "morning_log.csv"

# check device availability
def ensure_device():
    # list all devices
    devices = sp.devices()["devices"]
    # raise RuntimeError if no devices found
    if not devices:
        raise RuntimeError("No devices found. Open Spotify on your PC or phone first.")
    # choose first occurrence of active device OR choose first device from the list, return device
    device = next((d for d in devices if d["is_active"]),devices[0])
    return device

# pick random track from genre pre determined list
def pick_random_track(genre):
    # search for tracks that match this genre keyword
    results = sp.search(q=f"genre:{genre}", type="track", limit=50)
    tracks = results["tracks"]["items"]

    if not tracks:
        raise RuntimeError(f"No tracks found for genre '{genre}'")

    track = random.choice(tracks)
    name = track["name"]
    artists = ", ".join(a["name"] for a in track["artists"])
    uri = track["uri"]
    return name, artists, uri

# add the randomized track into song tracker csv
def log_play(name, artist, uri, genre):
    date = datetime.date.today().isoformat()
    new_file = not os.path.exists(log_file)
    with open(log_file, "a", encoding="utf-8") as f:
        if new_file:
            f.write("date,uri,name,artist,genre\n")
        f.write(f"{date},{uri},{name},{artist},{genre}\n")

def play_random_genre():
    genre = random.choice(user_genres)
    name, artist, uri = pick_random_track(genre)
    device = ensure_device()
    sp.start_playback(uris=[uri])
    log_play(name, artist, uri, genre)
    print(f"[{genre}] Now playing: {name} — {artist} on {device['name']}")

if __name__ == "__main__":
    play_random_genre()
