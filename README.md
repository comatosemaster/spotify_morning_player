Spotify Morning Auto-Play 🎧

A Python automation script that starts Spotify every morning, activates playback,
and plays a random song from your favorite genre automatically.

✨ Features

🚀 Launches Spotify automatically.

🎶 Picks a random song from specified genres.

🧾 Logs each morning's track to a CSV file.

🕙 Fully compatible with Windows Task Scheduler for daily runs.


⚙️ Setup

1️⃣ Clone the repository

git clone https://github.com/comatosemaster/spotify_morning_player.git

cd spotify_morning_player

2️⃣ Create a .env file

Create a file named .env in the root directory and add your Spotify API credentials:

SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://127.0.0.1:8888/callback

3️⃣ Install dependencies

pip install -r requirements.txt

4️⃣ Run manually

python morning_player.py

5️⃣ (Optional) Automate with Task Scheduler

Use launcher.bat to have the script run automatically every morning via
Windows Task Scheduler or Startup Folder.

📝 Notes

Requires a Spotify Premium account for playback control.

.env, .cache, and log files are intentionally excluded from GitHub for security.

Works best when Spotify desktop app is already installed and logged in.

🧩 Example log entry

2025-10-26,spotify:track:3AJwUDP919kvQ9QcozQPxg,Shape of You,Ed Sheeran,Pop

🧠 Author

Davit Mujirishvili (@comatosemaster)
🎧 Automating good mornings since 2025
