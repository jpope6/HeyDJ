import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

SCOPEs = [
    'app-remote-control',
    'user-read-playback-state',
    'user-modify-playback-state',
    'user-read-currently-playing'
]


class Spotify:


    def __init__(self) -> None:
        self.spotify = self.authenticateSpotify()

    def authenticateSpotify(self):
        auth = SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=SCOPEs
        )
        sp = spotipy.Spotify(auth_manager=auth)

        return sp

    def runCommand(self, command):
        if "start" in command:
            self.spotify.start_playback()
            print("play")
        elif "stop" in command:
            self.spotify.pause_playback()
            print("pause")
