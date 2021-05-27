import os
import time
import pyttsx3
import speech_recognition as sr
import subprocess
import datetime

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[31].id)


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[31].id)
    # Voz Hombre.
    # engine.setProperty('voice', voices[15].id)
    engine.say(text)
    engine.runAndWait()


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio, language="es-MX")
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said.lower()

def notes(text):
    with open(("mis_notas.txt"), "a+", encoding='ISO-8859-1') as mis_notas:
        mis_notas.write(str(datetime.date.today()) + "\n")
        mis_notas.write(text + "\n\n")



def abrir_notes():
    subprocess.call(['open', '-a', 'TextEdit', "mis_notas.txt"])





print("Di algo...")
WAKE =  "oye peyton"

while True:

    text = get_audio()

    if text.count(WAKE) > 0:
        speak("¿dime?")
        text = get_audio()

        # CREAR_NOTAS = ["crea una nota"]
        # for frases in CREAR_NOTAS:
        #     if frases in text:
        #         speak("¿Qué quieres que escriba?")
        #         note = get_audio().lower()
        #         notes(note)
        #         speak("He creado la nota")
        #
        # ABRIR_NOTAS = ["abrir mis notas"]
        # for frases in ABRIR_NOTAS:
        #     if frases in text:
        #         speak("Aquí están tus notas")
        #         abrir_notes

        if "crea una nota" in text:
            speak("¿Qué quieres que escriba?")
            note = get_audio().lower()
            notes(note)
            speak("He creado la nota")

        if "abrir mis notas" in text:
            speak("Aquí estan tus notas")
            abrir_notes


        if "hola" in text:
            speak("Hola, ¿Cómo estás?")

        if "cómo estás" in text:
            speak("Muy bien, gracias!")

        if "cómo te llamas" in text:
            speak("Mi nombre es péiton")

        if "cuál es tu nombre" in text:
            speak("Mi nombre es peyton")

        if "adiós" in text:
            speak("Chao")

        if "creador" in text:
            speak("Mi creador es Manuel")

        if ("saluda a merly") in text:
            speak("Hola Merly")

        if ("saluda a merli") in text:
            speak("Hola Merly")

        # Agregar una nota.


