import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import json

load_dotenv()

SCOPEs = [
    "app-remote-control",
    "user-read-playback-state",
    "user-modify-playback-state",
    "user-read-currently-playing",
]


class Spotify:
    def __init__(self) -> None:
        self.spotify = self.authenticateSpotify()

    def authenticateSpotify(self):
        auth = SpotifyOAuth(
            client_id=os.getenv("SPOTIPY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
            scope=SCOPEs,
        )
        sp = spotipy.Spotify(auth_manager=auth)

        return sp

    def runCommand(self, json_command):
        command = json.loads(json_command)
        print(command)

        match command.get("action"):
            case "play" | "resume":
                track_uri = self.getTrackURI(command.get("song"), command.get("artist"))
                self.playTrack(track_uri)
            case "pause":
                self.pauseTrack()
            case "add_to_queue":
                track_uri = self.getTrackURI(command.get("song"), command.get("artist"))
                self.addTrackToQueue(track_uri)
            case "skip" | "next":
                self.skipSong()

    def getTrackURI(self, track_name, artist_name):
        if not track_name and not artist_name:
            return None

        results = self.spotify.search(q=f"{track_name} {artist_name}", type="track")

        if results["tracks"]["items"]:
            # Get the URI of the first track in the search results
            track_uri = results["tracks"]["items"][0]["uri"]
            return track_uri

        print(f"Track {track_name} by {artist_name} not found.")
        return None

    def playTrack(self, track_uri):
        if track_uri:  # User has requested a specific song
            self.spotify.start_playback(uris=[track_uri], position_ms=0)
        else:  # User has not requested any specific song
            self.spotify.start_playback()

    def pauseTrack(self):
        self.spotify.pause_playback()

    def addTrackToQueue(self, track_uri):
        if not track_uri:
            return

        self.spotify.add_to_queue(uri=track_uri)

    def skipSong(self):
        self.spotify.next_track()
