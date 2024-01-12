from speech import Speech
from spotify import Spotify
from chatgpt import ChatGPT


class Main:
    def __init__(self) -> None:
        self.spotify = Spotify()
        self.chatGPT = ChatGPT()
        self.speech = Speech()
        self.running = True

    def run(self):
        while self.running:
            self.speech.listen()
            command = self.speech.recognizeSpeech()

            if command:
                ai_response = self.chatGPT.sendMessageToAI(command)
                self.spotify.runCommand(ai_response)


def main():
    m = Main()
    m.run()


if __name__ == "__main__":
    main()
