import speech_recognition as sr
import pyaudio as pa
import sounddevice as sd 

def recognise(audio_url = 'assets/speech/audio.wav'):
    # create a speech recognition object
    r = sr.Recognizer()
    with sr.AudioFile(audio_url) as source:
        audio_data = r.record(source=source)

 
    
    try:
        text = r.recognize_google(audio_data, language="it-IT")
        return text
    except Exception as e:
        print(f"Error: {e}")
    
    

