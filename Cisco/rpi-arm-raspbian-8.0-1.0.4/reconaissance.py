from tkinter import *
import speech_recognition as sr
import os

def reconnaissance(): 
 r = sr.Recognizer()
 with sr.Microphone() as source:
   r.adjust_for_ambient_noise(source)  
   print("je t'écoute")
   audio = r.listen(source)
   try: 
    ua = (r.recognize_google( audio, language='fr-FR', show_all=False))
   except:
   	print("Pas compis mr le touton")

reconnaissance()




os.system("pause")

