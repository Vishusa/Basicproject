import speech_recognition as sr
import os
import win32com.client

# speaker = win32com.client.Dispatch("SAPI.Spvoice")
#
# while 1:
#     print("Enter the word you want to speak it out computer")
#     s = input()
#     speaker.speak(s)

def say(text):
    os.system(f"say {text}")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        query = r.recognize_google(audio , language="en-in")
        print(f" user said: {query}")
        return query

if __name__ == ' main':
    print("pycharm")
    say("Hello I am JARVIS A.I")
    while True:
        print("Listening...")
        text = takecommand()
        say(text)