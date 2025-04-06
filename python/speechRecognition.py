import speech_recognition as sr
import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

def record_audio(filename, duration=5, fs=44100):
    print("Recording... Speak now.")
    audio_data = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio_data)
    print("Recording complete and saved to", filename)

def voice_to_text(filename):

    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(filename) as source:
            print("Processing the audio file...")
            audio = recognizer.record(source)
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return None

if _name_ == "_main_":
    filename = "output.wav"
    record_audio(filename, duration=5)
    
    transcription = voice_to_text(filename)
    if transcription:
        print("Final Transcription:", transcription)