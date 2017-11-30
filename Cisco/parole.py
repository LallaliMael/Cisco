# -*- coding: utf-8 -*-

import pygame
from gtts import gTTS

nombre = 1
chemin = str(str(nombre) + ".mp3")
global nombre
global chemin

def dit(lire):
 print(chemin)
 tts = gTTS(text=lire, lang='fr')
 tts.save(chemin)
 pygame.mixer.init()
 pygame.mixer.music.load(chemin)
 nombre += 1
 pygame.mixer.music.play()
 while pygame.mixer.music.get_busy():
              pass 
 chemin = str(str(nombre) + ".mp3")
