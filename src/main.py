from speech import Speech
from spotify import Spotify


class Main:
    def __init__(self) -> None:
        self.speech = Speech()
        self.spotify = Spotify()
        self.running = True

    def run(self):
        while self.running:
            self.speech.obtainAudioFromMicrophone()
            command = self.speech.recognizeSpeech()

            if command:
                self.spotify.runCommand(command)


def main():
    m = Main()
    m.run()


if __name__ == "__main__":
    main()
