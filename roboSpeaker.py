import os
import win32com.client as wincom
print("Welcome to RoboSpeaker 1.1. Created by Anurag...")
while True:
    x = input("Enter what you want me to pronounce:  ")
    if x == "q":
        break
    speak = wincom.Dispatch("SAPI.SpVoice")
    speak.Speak(x)