import os
import win32com.client as wincom
speak = wincom.Dispatch("SAPI.SpVoice")
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Priya")
    while True:
        x = input("Enter what you want me to speak: ")
        if x=="q":
            speak.Speak("bye bye friend")
            break
        speak.Speak({x})

