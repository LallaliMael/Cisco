# -*- coding: utf-8 -*-

import pygame
from gtts import gTTS

nombre = 1
chemin = str(str(nombre) + ".mp3")
chemin_vers_dossier_synthese_vocale = "chemin_vers_votre_dossier_synthese_vocale"
chemine = ''
chemine = (chemin_vers_dossier_synthese_vocale + chemin)
nombre = 1


def dit(lire):
 print(chemin)
 tts = gTTS(text=lire, lang='fr')
 tts.save(chemine)
 pygame.mixer.init()
 pygame.mixer.music.load(chemine)
 nombre += 1
 pygame.mixer.music.play()
 while pygame.mixer.music.get_busy():
              pass 
 global nombre
 global chemin
 global chemine
 global chemin_vers_dossier_synthese_vocale
 chemin = str(str(nombre) + ".mp3")
 chemine = ''
 chemine = (chemin_vers_dossier_synthese_vocale + chemin)