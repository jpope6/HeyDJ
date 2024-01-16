from speech import Speech
from spotify import Spotify
from chatgpt import ChatGPT

ASCII_ART = """
  _    _              _____       _ 
 | |  | |            |  __ \     | |
 | |__| | ___ _   _  | |  | |    | |
 |  __  |/ _ \ | | | | |  | |_   | |
 | |  | |  __/ |_| | | |__| | |__| |
 |_|  |_|\___|\__, | |_____/ \____/ 
               __/ |                
              |___/                 
"""


class Main:
    def __init__(self) -> None:
        self.spotify = Spotify()
        self.chatGPT = ChatGPT()
        self.speech = Speech(self.spotify)

    def run(self):
        while self.spotify.running:
            self.speech.listen()
            command = self.speech.recognizeSpeech()

            if command:
                ai_response = self.chatGPT.sendMessageToAI(command)
                self.spotify.runCommand(ai_response)

        # Clean Up
        self.speech.porcupine.delete()
        self.speech.recorder.delete()


def main():
    print(ASCII_ART)
    print("Your personal AI powered Spotify assistant.")
    print('Say "Hey DJ" followed by a command to control your Spotify!')
    print("To exit the program, just saying 'Hey DJ, exit.'")

    m = Main()
    m.run()


if __name__ == "__main__":
    main()
