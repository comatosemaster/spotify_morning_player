@echo off
setlocal

:: Path to log file
set LOGFILE="C:\Users\Davit\PycharmProjects\Learning\Lots of stuff\Spotify API\launch_logs.log"

:: Add a timestamp header
echo ============================================== >> %LOGFILE%
echo [%date% %time%] Morning Auto-Play launched >> %LOGFILE%
echo ============================================== >> %LOGFILE%

echo Launching Spotify... >> %LOGFILE%
start "" "C:\Users\Davit\AppData\Local\Microsoft\WindowsApps\Spotify.exe"

:: Wait for Spotify to open
timeout /t 3 /nobreak >> %LOGFILE%

:: Change directory to project
cd "C:\Users\Davit\PycharmProjects\Learning\Lots of stuff\Spotify API"

:: Run Spotify activation (play → pause)
echo [%time%] Running spotify_autoplay.py >> %LOGFILE%
"C:\Users\Davit\PycharmProjects\Learning\.venv\Scripts\python.exe" spotify_autoplay.py >> %LOGFILE% 2>&1

:: Wait for device registration
timeout /t 1 /nobreak >> %LOGFILE%

:: Run morning player
echo [%time%] Running morning_player.py >> %LOGFILE%
"C:\Users\Davit\PycharmProjects\Learning\.venv\Scripts\python.exe" morning_player.py >> %LOGFILE% 2>&1

echo [%time%] Morning Auto-Play finished >> %LOGFILE%
echo. >> %LOGFILE%

endlocal
exit