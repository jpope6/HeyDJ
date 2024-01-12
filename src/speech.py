import speech_recognition as sr
import sounddevice  # Not used in code but it stops ALSA error from speech recoginition
import re


class Speech:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.audio = None

        self.phrase = "hey dj"

    def obtainAudioFromMicrophone(self):
        with sr.Microphone() as source:
            print("Say something!")

            while True:
                self.audio = self.recognizer.listen(source)

                if self.isPhraseDetected():
                    print("It has been said. I am awaken.")
                    break

    def isPhraseDetected(self):
        try:
            command = self.recognizer.recognize_whisper(self.audio, language="english")
            return self.phrase in command.lower()

        except sr.UnknownValueError:
            pass

        return False

    def recognizeSpeech(self):
        if not self.audio:
            return None

        try:
            command = self.recognizer.recognize_whisper(self.audio)

            # regex to remove everything before and including the phrase "hey dj"
            # regex_pattern = rf".*?{re.escape(self.phrase)}"
            # modified_command = re.sub(regex_pattern, "", command.lower())

            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Error; {0}".format(e))
            return None
