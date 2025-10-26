import pyautogui
import time
import os
import subprocess

print("Waiting for Spotify to launch...")
time.sleep(8)

# Optional: check if Spotify process exists
try:
    # Works on Windows: checks if "Spotify.exe" is in running processes
    output = subprocess.check_output('tasklist', shell=True).decode()
    if "Spotify.exe" not in output:
        print("Spotify not found running.")
        raise SystemExit(1)
except Exception as e:
    print("Could not verify Spotify process:", e)

# Press space once to start playback
print("Sending PLAY command to Spotify...")
pyautogui.hotkey('space')
# wait a moment for playback to register

# Press space again to pause
print("Sending PAUSE command to Spotify...")
pyautogui.hotkey('space')

print("Spotify should now be active and ready for API control.")