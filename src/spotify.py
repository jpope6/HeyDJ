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
        self.running = True

    def authenticateSpotify(self):
        auth = SpotifyOAuth(
            client_id=os.getenv("SPOTIFY_CLIENT_ID"),
            client_secret=os.getenv("SPOTIFY_CLIENT_SECRET"),
            redirect_uri=os.getenv("SPOTIFY_REDIRECT_URI"),
            scope=SCOPEs,
        )
        sp = spotipy.Spotify(auth_manager=auth)

        return sp

    def runCommand(self, json_command):
        command = json.loads(json_command)
        song = command.get("song")
        artist = command.get("artist")
        # print(command)

        action = command.get("action")

        if action in {"play", "resume"}:
            track_uri = self.getTrackURI(song, artist)
            self.playTrack(track_uri, song, artist)
        elif action == "pause":
            self.pauseTrack()
        elif action in {"add_to_queue", "add to queue"}:
            track_uri = self.getTrackURI(song, artist)
            self.addTrackToQueue(track_uri, song, artist)
        elif action in {"skip", "next"}:
            self.skipSong()
        elif action in {"previous", "back"}:
            self.previousTrack()
        elif action in {"exit", "quit"}:
            self.running = False

    def getTrackURI(self, track_name, artist_name):
        try:
            if not track_name and not artist_name:
                return None

            results = self.spotify.search(q=f"{track_name} {artist_name}", type="track")

            if results and results["tracks"]["items"]:
                # Get the URI of the first track in the search results
                track_uri = results["tracks"]["items"][0]["uri"]
                return track_uri

            print(f"Track {track_name} by {artist_name} not found.")
            return None

        except spotipy.SpotifyException as e:
            print(f"Spotify API error in getTrackURI: {e}")
            return None

    def playTrack(self, track_uri, song, artist):
        try:
            if track_uri:  # User has requested a specific song
                self.spotify.start_playback(uris=[track_uri], position_ms=0)

                if song and artist:
                    print(f"Now playing {song} by {artist}.")
                elif song:
                    print(f"Now playing {song}.")
                elif artist:
                    print(f"Now playing {artist}.")

            else:  # User has not requested any specific song
                self.spotify.start_playback()
                print("Resuming playback.")

        except spotipy.SpotifyException as e:
            print(f"Spotify API error in playTrack: {e}")

    def pauseTrack(self):
        try:
            self.spotify.pause_playback()
            print("Pausing playback.")

        except spotipy.SpotifyException as e:
            print(f"Spotify API error in pauseTrack: {e}")

    def addTrackToQueue(self, track_uri, song, artist):
        try:
            if not track_uri:
                return

            self.spotify.add_to_queue(uri=track_uri)

            if song and artist:
                print(f"Adding {song} by {artist} to the queue.")
            elif song:
                print(f"Adding {song} to the queue.")
            elif artist:
                print(f"Adding {artist} to the queue.")

        except spotipy.SpotifyException as e:
            print(f"Spotify API error in addTrackToQueue: {e}")

    def skipSong(self):
        try:
            self.spotify.next_track()
            print("Skipping song...")

        except spotipy.SpotifyException as e:
            print(f"Spotify API error in skipSong: {e}")

    def previousTrack(self):
        try:
            self.spotify.previous_track()
            print("Playing previous song...")

        except spotipy.SpotifyException as e:
            print(f"Spotify API error in previousTrack: {e}")

    def changeVolume(self, volume_percentage):
        self.spotify.volume(volume_percentage)

    def getCurrentVolume(self) -> int:
        current_playback = self.spotify.current_playback()

        if not current_playback:
            return 0

        current_volume = current_playback["device"]["volume_percent"]
        return current_volume
