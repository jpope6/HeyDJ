import speech_recognition as sr

class Speech:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.audio = None

    def obtainAudioFromMicrophone(self):
        with sr.Microphone() as source:
            print("Say something!")
            self.audio = self.recognizer.listen(source)

    def recognizeSpeech(self):
        if not self.audio:
            return None

        try:
            command = self.recognizer.recognize_sphinx(self.audio)
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Error; {0}".format(e)) 
            return None
