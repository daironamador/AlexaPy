import speech_recognition as sr
import pyttsx3



recognizer = sr.Recognizer()


engine = pyttsx3.init()

#voices = engine.getProperty('voices')
#engine.setProperty('voice',voices[1].id)

#engine.say("Buenas Noches")
#engine.runAndWait()

def record_audio():
    with sr.Microphone() as source:
        eng("Escuchando...")
        audio = recognizer.listen(source)
    return audio

def recognize_speech(audio):
    try:
        text = recognizer.recognize_google(audio)
        print(f"Dijiste: {text}")
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
    except sr.RequestError:
        print("Sorry, there was an error processing your request.")

if __name__ == "__main__":
    audio = record_audio()
    recognize_speech(audio)
    