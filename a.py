"""NOT WORKING SO FAR"""


import speech_recognition as sr
from googletrans import Translator

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please grant microphone access and speak...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Processing...")
            text = recognizer.recognize_google(audio, language='en')
            print("Recognized Text (English):", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand the audio.")
        except sr.RequestError:
            print("Could not request results, please check your internet connection.")
    return None

def translate_to_hindi(text):
    if text:
        translator = Translator()
        translated = translator.translate(text, dest='hi')
        print("Translated Text (Hindi):", translated.text)
        return translated.text
    return None

if __name__ == "__main__":
    text = recognize_speech()
    translate_to_hindi(text)


