import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()



engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

engine.say("Buenas Noches")
engine.runAndWait()


try:
    with sr.Microphone() as source:
        engine.say("Escuchando...")
        voice = listener.listen(source)
        rec = listener.recognize_google(voice)
        print(rec)   
except: 
    pass