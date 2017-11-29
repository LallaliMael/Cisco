import os
import pygame


def lecture_musique():
   global phrase
   fichier = os.listdir(chemin_vers_votre_dossier_musique)
   nombre = len(fichier)
   dossier = (chemin_vers_votre_dossier_musique)
   pygame.mixer.init()
   compteurmusique = 1
   global compteurmusique
   for mot in fichier:
     chemin = dossier + mot
     if mode_musique = 1:
      pygame.mixer.music.pause()
     if (".mp3") in chemin and mode_musique == 2 or (".wav") in chemin and mo == 2:
      if compteurmusique == 1:       
       pygame.mixer.music.load(chemin)
       pygame.mixer.music.play()
       while pygame.mixer.music.get_busy():
          pass
   if ("suivante") in phrase phrase and ("stop") not in phrase:
    pygame.mixer.music.stop()
     

def reconnaissance_musique()
 while(1)
  r = sr.Recognizer()
  r.energy_threshold = 525
  with sr.Microphone() as source:  
   print("je vous écoutes")
   audio = r.listen(source)
   print("réfléxion")
   try: 
    detection = (r.recognize_google( audio, language='fr-FR', show_all=False))
    if "cisco" in detection and "stop" in detection:
     mode_musique = 1  
     break
    elif "cisco" in detection and "suivante" in detection and "musique" in detection:
     mode_musique = 2
   except:
    None  