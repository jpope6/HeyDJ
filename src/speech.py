import speech_recognition as sr
import sounddevice  # Not used in code but it stops ALSA error from speech recoginition
import pvporcupine
from pvrecorder import PvRecorder
import os
from dotenv import load_dotenv

load_dotenv()


class Speech:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()
        self.audio = None

        self.phrase = "hey dj"

        self.porcupine = pvporcupine.create(
            access_key=os.getenv("PORCUPINE_ACCESS_KEY"),
            keyword_paths=["./Hey-DJ_en_linux_v3_0_0.ppn"],
        )
        self.recorder = PvRecorder(frame_length=512)

    def listen(self):
        self.recorder.start()
        audio_frame = self.recorder.read()
        keyword_index = self.porcupine.process(audio_frame)
        if keyword_index == 0:  # Wake word indentified
            print("obtaining audio")
            self.obtainAudioFromMicrophone()

    def obtainAudioFromMicrophone(self):
        with sr.Microphone() as source:
            self.audio = self.recognizer.listen(source)

    def recognizeSpeech(self):
        if not self.audio:
            return None

        try:
            command = self.recognizer.recognize_whisper(self.audio)
            self.audio = None  # Reset the audio
            print("You said: " + command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print("Error; {0}".format(e))
            return None
