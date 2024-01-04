from speech import Speech
from spotify import Spotify

class Main:
    def __init__(self) -> None:
        self.speech = Speech()
        self.spotify = Spotify()
        
        self.running = True

    def run(self):
        self.speech.obtainAudioFromMicrophone()
        command = self.speech.recognizeSpeech()

        if command:
            if "exit" in command:
                self.running = False

            self.spotify.runCommand(command)

def main():
    m = Main()

    while m.running:
        m.run()

if __name__ == "__main__":
    main()
