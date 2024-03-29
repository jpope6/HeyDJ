import speech_recognition as sr
import sounddevice  # Not used in code but it stops ALSA error from speech recoginition
import pvporcupine
from pvrecorder import PvRecorder
import os
from dotenv import load_dotenv
import platform

load_dotenv()


class Speech:
    def __init__(self, spotify) -> None:
        self.recognizer = sr.Recognizer()
        self.audio = None

        keyword_file_path = ""

        if platform.system() == "Linux":
            keyword_file_path = "./training-data/Hey-DJ_en_linux_v3_0_0.ppn"
        elif platform.system() == "Windows":
            keyword_file_path = "./training-data/Hey-DJ_en_windows_v3_0_0.ppn"
        elif platform.system() == "Darwin":  # macOS
            keyword_file_path = "./training-data/Hey-DJ_en_mac_v3_0_0.ppn"
        else:
            # Handle other operating systems or raise an exception if not supported
            raise Exception("Unsupported operating system")
        
        self.porcupine = pvporcupine.create(
            access_key=os.getenv("PICOVOICE_ACCESS_KEY"),
            keyword_paths=[keyword_file_path],
        )

        self.recorder = PvRecorder(frame_length=512)
        self.spotify = spotify

    def listen(self):
        self.recorder.start()
        audio_frame = self.recorder.read()
        keyword_index = self.porcupine.process(audio_frame)
        if keyword_index == 0:  # Wake word indentified
            print("\nListening...")
            self.obtainAudioFromMicrophone()

    def obtainAudioFromMicrophone(self):
        current_volume = self.spotify.getCurrentVolume()

        # Mute spotify so the microphone does not pick it up
        self.spotify.changeVolume(0)

        with sr.Microphone() as source:
            self.audio = self.recognizer.listen(source)

        # Reset to original volume
        self.spotify.changeVolume(current_volume)

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
